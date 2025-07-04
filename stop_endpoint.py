# Stop the SageMaker endpoint (remove it and its config) to save cost
import boto3

region = "us-east-2"
endpoint_name = "aml-fraud-detector-endpoint"

client = boto3.client("sagemaker", region_name=region)

try:
    client.delete_endpoint(EndpointName=endpoint_name)
    client.delete_endpoint_config(EndpointConfigName=endpoint_name)
    print(f"✅ Endpoint '{endpoint_name}' and its config deleted successfully.")
except client.exceptions.ClientError as e:
    print(f"⚠️ Failed to delete endpoint or config: {e}")
