import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3():
    # Load AWS Credentials from .env
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = os.getenv('AWS_REGION', 'eu-central-1')
    bucket_name = os.getenv('AWS_S3_BUCKET', 'celonis-hr-demo-bucket')
    
    file_to_upload = 'data/harmonized_eventlog.csv'
    object_name = 'raw/hr_process_mining/harmonized_eventlog.csv'
    
    if not os.path.exists(file_to_upload):
        print(f"Error: {file_to_upload} not found. Run script 03 first.")
        return

    # Check if we have credentials
    if not access_key or not secret_key or access_key == 'AKIAXXXXXXXXXXXXXXXX':
        print("MOCK: AWS Credentials not configured in .env. Simulating upload...")
        print(f"MOCK: Would upload {file_to_upload} to s3://{bucket_name}/{object_name}")
        return

    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        
        print(f"Uploading {file_to_upload} to s3://{bucket_name}/{object_name}...")
        s3_client.upload_file(file_to_upload, bucket_name, object_name)
        print("Upload Successful!")
        
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    upload_to_s3()
