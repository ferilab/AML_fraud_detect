
import boto3
import json

runtime = boto3.client('sagemaker-runtime', region_name='us-east-2')

payload = {
    "features": [1223.25, 2, 4, 3, 5, 7, 1, 3, 0, 6, 12, 3, 8]  # Replace with real feature values
}

response = runtime.invoke_endpoint(
    EndpointName='aml-fraud-endpoint',
    ContentType='application/json',
    Body=json.dumps(payload)
)

print(response['Body'].read().decode())
