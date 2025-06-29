
import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn


def launch_training_job():
    role = "arn:aws:iam::990682088412:role/SageMakerExecutionRole_AML"  # Replace this with your own ARN
    s3_input_path = "s3://aml-model-bk/data/"
    s3_output_path = "s3://aml-model-bk/output/"

    boto3.setup_default_session(region_name='us-east-2') 
    session = sagemaker.Session()

    estimator = SKLearn(
        entry_point="src/sagemaker_train.py",
        role=role,
        instance_type="ml.m5.large",
        framework_version="1.0-1",
        sagemaker_session=session,
        output_path=s3_output_path,
        base_job_name="aml-fraud-detect",
    )

    estimator.fit({"train": s3_input_path})

if __name__ == "__main__":
    launch_training_job()
