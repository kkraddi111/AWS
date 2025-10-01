import boto3
from botocore.exceptions import ClientError

AWS_REGION = "ap-south-1"
DEFAULT_BUCKET_NAME = "s3-ops"

def create_s3_client(region=AWS_REGION):
    return boto3.client('s3', region_name=region)

def create_bucket(bucket_name=DEFAULT_BUCKET_NAME, region=AWS_REGION):
    s3 = create_s3_client(region)
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        return True, f"Bucket '{bucket_name}' created successfully."
    except ClientError as e:
        return False, f"Error creating bucket: {e}"

def upload_file(bucket_name=DEFAULT_BUCKET_NAME, file_path=None, object_name=None):
    s3 = create_s3_client()
    if object_name is None and file_path is not None:
        object_name = file_path
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        return True, f"Uploaded '{file_path}' as '{object_name}' to '{bucket_name}'."
    except ClientError as e:
        return False, f"Error uploading file: {e}"

def download_file(bucket_name=DEFAULT_BUCKET_NAME, object_name=None, download_path=None):
    s3 = create_s3_client()
    try:
        s3.download_file(bucket_name, object_name, download_path)
        return True, f"Downloaded '{object_name}' from '{bucket_name}' to '{download_path}'."
    except ClientError as e:
        return False, f"Error downloading file: {e}"

def delete_file(bucket_name=DEFAULT_BUCKET_NAME, object_name=None):
    s3 = create_s3_client()
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        return True, f"Deleted '{object_name}' from '{bucket_name}'."
    except ClientError as e:
        return False, f"Error deleting file: {e}"
