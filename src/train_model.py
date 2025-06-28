import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.preprocess import load_and_clean_data

def train_and_save_model(data_path, model_path='models/aml_model.pkl'):
    print(f"Loading data from: {data_path}")
    X, y = load_and_clean_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.2, random_state=42
    )

    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Evaluation Report:\n")
    print('-' * 50)
    print(classification_report(y_test, y_pred, target_names=['Legal', 'Illegal']))

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model('data/global_black_money_transactions.csv')
