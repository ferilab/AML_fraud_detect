
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

sample_input = {
    "features": [
        12,      # Country
        10000,   # Amount (USD)
        1,       # Transaction Type
        23,      # Person Involved
        7,       # Industry
        18,      # Destination Country
        0,       # Reported by Authority
        6,       # Money Laundering Risk Score
        9,       # Shell Companies Involved
        4,       # Financial Institution
        0,       # Tax Haven Country
        6,       # Month
        15,      # Day
        2        # Weekday
    ]
}

def predict(sample_input, model_path='models/aml_model.pkl'):
    model = joblib.load(model_path)
    prediction = model.predict(sample_input)
    print('The prediction for this transaction is:   ', 'Illegal' if prediction == 1 else 'Legal')

if __name__ == '__main__':
    predict(np.array(sample_input['features']).reshape(1, -1))