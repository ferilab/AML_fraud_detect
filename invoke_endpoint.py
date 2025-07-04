
import boto3
import json

# Same endpoint and region
region = "us-east-2"
endpoint_name = "aml-fraud-detector-endpoint"

# Payload MUST match model's expected shape (14 features in same order)
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

# Call SageMaker endpoint
client = boto3.client("sagemaker-runtime", region_name=region)
response = client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/json",
    Body=json.dumps(sample_input)
)

# Get result
result = response["Body"].read().decode()
print("✅ Prediction:", result)
