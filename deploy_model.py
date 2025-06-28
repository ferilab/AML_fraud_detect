
import boto3
import sagemaker
from sagemaker.sklearn.model import SKLearnModel

# Define S3 model path
model_data = 's3://aml-model-bk/output/aml-detect-job/output/model.tar.gz'  # Adjust job name as needed

# SageMaker setup
role = "arn:aws:iam::990682088412:role/SageMakerExecutionRole_AML"  # Replace with  your sagemaker role ARM
region = "us-east-2"
session = sagemaker.Session()
sklearn_model = SKLearnModel(
    model_data=model_data,
    role=role,
    entry_point='src/sagemaker_train.py',
    framework_version='1.0-1',
    sagemaker_session=session
)

# Deploy to real-time endpoint
predictor = sklearn_model.deploy(
    instance_type='ml.t2.medium',
    initial_instance_count=1,
    endpoint_name='aml-fraud-endpoint'
)

print("✅ Endpoint deployed as: aml-fraud-endpoint")
