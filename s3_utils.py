
import os
import boto3
import kaggle

# Note: See the guide at the bottom

def upload_to_s3(local_path, bucket_name, s3_key):
    
    # Download the dataset from Kaggle
    # Note: If you prefer to directly read the data file from data folder only comment out the below kaggle.api
    # line. Just make sure you already have the data file 'Big_Black_Money_Dataset.csv' in the data folder
    kaggle.api.dataset_download_files('waqi786/global-black-money-transactions-dataset',
                                       path='data/', unzip=True)
    
    # Upload the dataset to our bucket on S3
    s3 = boto3.client('s3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name='us-east-2')
    
    s3.upload_file(local_path, bucket_name, s3_key)
    print(f"✅ Uploaded: s3://{bucket_name}/{s3_key}")

