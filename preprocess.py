
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date of Transaction'])

    # Drop rows with missing critical values
    df = df.dropna(subset=['Amount (USD)', 'Country', 'Source of Money'])

    # Remove transaction ID (non-informative)
    df = df.drop(columns=['Transaction ID'], errors='ignore')

    # Encode date into features (optional)
    df['Transaction Month'] = df['Date of Transaction'].dt.month
    df['Transaction Day'] = df['Date of Transaction'].dt.day
    df['Transaction Weekday'] = df['Date of Transaction'].dt.weekday
    df = df.drop(columns=['Date of Transaction'])

    # Encode categorical variables
    cat_cols = [
        'Country', 'Transaction Type', 'Person Involved', 'Industry',
        'Destination Country', 'Reported by Authority', 'Financial Institution',
        'Tax Haven Country'
    ]
    for col in cat_cols:
        df[col] = df[col].astype('category').cat.codes

    # Define features and target
    X = df.drop(columns=['Source of Money'])
    y = df['Source of Money'].apply(lambda x: 1 if x == 'Illegal' else 0)

    return X, y

