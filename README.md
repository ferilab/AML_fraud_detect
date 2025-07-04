# AML_fraud_detect

This Anti Money Laundering (AML) and fraud detection model performs risk assessment on international financial transactions. It is deployed on AWS S3 and SageMaker and uses GitHub Action for CI/CD.  

A full real-time fraud detection pipeline:

  - trigger the ETL by reading data directly from Kaggle or data folder of repository, uploading it to 
  - preparing data for model training
  - model training/validation on SageMaker, and uploding data and model to S3. All steps up to here with pushing updated repo to GitHub
  - Store model in S3
  - Deploy model on SageMaker Real-time endpoint for inference via AWS CLI
  - Real-time prediction with CLI
  - Cost control via manual endpoint shutdown

# Dataset

This dataset provides 10,000 financial transactions across multiple countries, focusing on risk assessment and fraud detection. It is important to explore patterns in financial movements, assess money laundering risks, and develop anti-money laundering (AML) models.

With comprehensive attributes such as transaction amounts, risk scores, and entity involvement, this dataset serves as a valuable resource for understanding financial irregularities and compliance monitoring. 

# Project structure

aml_fraud_detect/
├── data/
│   └── Big_Black_Money_Dataset.csv
├── src/
│   ├── __init__.py
│   ├── train_model.py      # Train and save ML model locally
│   └── predict.py          # Local inference with the local model: python predict.py
├── .github/workflows/
│   └── train.yml           # GitHub Actions workflow
├── sagemaker_train.py      # Runs SageMaker training job on SageMaker
├── sagemaker_launcher.py   # Launch SageMaker training job
├── deploy_model.py         # Create endpoint for real-time inference on SageMaker
├── invoke_endpoint.py      # Inference on a new transaction
├── stop_endpoint.py        # Stop the SageMaker real-time endpoint
├── s3_utils.py             # Upload/download from S3
├── preprocess.py           # prepares the dataset on Sagemaker for training job
├── inference.py
├── main.py                 # For local run: python main.py
├── models/                 # Reserved for local use
├── requirements.txt
└── README.md


# Process 

The process flow can be summarized as follows:

  A[Push to GitHub] --> B[GitHub Actions: train.yml]
  B --> C[s3_utils.py uploads dataset to S3]
  C --> D[sagemaker_launcher.py launches training job (sagemaker_train.py and preprocess.py)]
  D --> E[Trained model saved to S3 by sagemaker_launcher.py]
  E --> F[deploy_model.py deploys SageMaker endpoint]
  F --> G[invoke_endpoint.py sends input (new data for inference)]
  G --> H[Model returns prediction]
  H --> I[stop_endpoint.py shuts down endpoint to save cost]
  I --> F[*** Restart the endpoint if required using deploy_model.py]


# Cloud setup (AWS)

You first need to fork the repo to your personal GitHub account. This repo will do the CI/CD including training and retraining of the model for you.

1. Create an AWS account (a free trail if you already don't have)

2. Sign in with your IAM acccount

3. Give it full role access.

4. Creats a bucket in S3 (we named it aml-model-bk, you can make yours and update the code accordingly).

5. Go to your AWS IAM Console, under Access Keys click Create access key and choose Command Line Interface (CLI). Now create access key and save the key id and access key. Then, set the secrets of your cloned repository (Settings - Secrets and variables - Actions). Name them AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION (the region you choose for your S3 bucket).

6. Create SageMaker Execution Role

Go to IAM - Roles
Click Create role > Use case: SageMaker
Attach policies:  AmazonSageMakerFullAccess    and     AmazonS3FullAccess (or scoped to your bucket)
Name it (e.g., SageMakerExecutionRole_AML) and copy the Role ARN

7. Set Up AWS CLI (to start or stop the real-time endpoint from your terminal)

Type 'aws configure' in terminal
You’ll be prompted for:
AWS Access Key ID
AWS Secret Access Key
Default region name: us-east-2 (your region)
Output format: json (or just press Enter)


8. Dependencies

- For cloud use, they will be installed by the pipeline module (train.yml), however, for inference you'll need to have them installed on your local drive.
- For local use, you'll need to create a virtual environment, activate it and install requirements.txt

9. Trigger Training on GitHub Push

After creating the AWS services as explained above commit and push the repository to your GitHub account. Then:

- CI/CD is handled via .github/workflows/train.yml
- Uploads dataset using s3_utils.py
- Triggers training using sagemaker_launcher.py
- Saves trained model as model.tar.gz in S3

10. Deploy Model to Real-Time Endpoint

Running this in terminal:
python deploy_model.py
will (takes several minutes):

- Loads trained model from S3
- Deploys using inference.py
- Creates endpoint: aml-fraud-detector-endpoint (or the name you chave chosen for it)

# Real-time Inference 

Run this in terminal:
python invoke_endpoint.py

The module includes a sample transaction. You can manipulate the values. Note that the structure of the sample and variable names must be preserved.


# Stop Endpoint to Save Cost

Use in terminal:
python stop_endpoint.py

The most costly part of the AWS services is the endpoint here. Stop it once you finished your tests. The storage is very cheap and you can keep it for a while until you decide to remove the services completely.

git clone https://github.com/ferilab/aml_fraud_detect.git
cd aml_fraud_detect

# Model Details

- Algorithm: RandomForestClassifier
- Target Variable: Source of Money (0 = Legal, 1 = Illegal)
- Feature Engineering: Extracted from transaction date and encoded categoricals
- Training Script: sagemaker_train.py
- Inference Logic: inference.py

# Further improvements

Some other features that can be added to this application are:

- Streamlit frontend for input + results
- Deploy behind API Gateway for public access (will be costly))
- Add CloudWatch monitoring and alerts

# Notes

- The package is compatible with AWS Free Tier