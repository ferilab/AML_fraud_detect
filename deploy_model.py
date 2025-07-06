
import boto3
import sagemaker
from sagemaker.sklearn.model import SKLearnModel

# Set region and session
boto3.setup_default_session(region_name="us-east-2")
sagemaker_session = sagemaker.Session()

# SageMaker role
role = "arn:aws:iam::990682088412:role/SageMakerExecutionRole_AML"  # Replace with your IAM role's arn

# Trained model path in S3 (replace with actual job output)
aml_detect_job = "aml-fraud-detect-2025-07-04-13-46-28-830" # Adjust job name as needed
model_s3_path = 's3://aml-model-bk/output/' + aml_detect_job + '/output/model.tar.gz'  

# Create SKLearnModel from the trained model
model = SKLearnModel(
    model_data=model_s3_path,
    role=role,
    framework_version="1.0-1",
    entry_point="inference.py",  # Needed for inference logic
    source_dir='.',  # Includes preprocess.py if needed
    sagemaker_session=sagemaker_session
)

# Deploy to an endpoint
predictor = model.deploy(
    instance_type="ml.t2.medium", # Hosting is faster but costier with ml.m5.large
    initial_instance_count=1,
    endpoint_name="aml-fraud-detector-endpoint"
)

print("✅ Model deployed to endpoint: aml-fraud-detector-endpoint")
