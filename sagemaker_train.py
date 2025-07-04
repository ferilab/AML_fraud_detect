
import argparse
import os
import joblib
import pandas as pd
from preprocess import load_and_clean_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # Tell SageMaker where to find training data and where to save the trained model, 
    # using its built-in environment variables:
        # SM_CHANNEL_TRAIN → input data path in container
        # SM_MODEL_DIR → output path for the trained model
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--data-dir', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    args = parser.parse_args()

    # Read data from SageMaker input channel
    data_path = os.path.join(args.data_dir, 'Big_Black_Money_Dataset.csv')
    
    print(f"Looking for data at {data_path}")
    print(f"Directory listing: {os.listdir(args.data_dir)}")

    X, y = load_and_clean_data(data_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)

    model = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    model_output_path = os.path.join(args.output_dir, 'model.joblib')
    joblib.dump(model, model_output_path)
    print(f"Model saved to {model_output_path}")
