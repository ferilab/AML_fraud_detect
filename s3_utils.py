
import boto3
# import kaggle

# Note: See the guide at the bottom

def upload_to_s3(local_path, bucket_name, s3_key):
    
    # Download the dataset from Kaggle
    # kaggle.api.dataset_download_files('waqi786/global-black-money-transactions-dataset',
                                    #    path='data/', unzip=True)
    # Upload the dataset to our bucket on S3
    s3 = boto3.client('s3',
        aws_access_key_id='AKIA6NKKBAPOEGABOVJC',
        aws_secret_access_key='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',
        region_name='us-east-2')
    s3.upload_file(local_path, bucket_name, s3_key)
    print(f"✅ Uploaded: s3://{bucket_name}/{s3_key}")


'''
Use this module to get the file from Kaggle and then upload it to S3.

in cLI (while your in your package root and the virtual env is activated):
aws configure
You’ll be prompted for:

    AWS Access Key ID

    AWS Secret Access Key

    Default region name: us-east-2 (your region)

    Output format: json (or just press Enter)
python -c "from s3_utils import upload_to_s3; upload_to_s3('data/Big_Black_Money_Dataset.csv', 'your-bucket-name', 'data/Big_Black_Money_Dataset.csv')"

'''
