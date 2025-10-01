import streamlit as st
import os
import boto3
from botocore.exceptions import ClientError
from s3_operations import create_bucket, upload_file, download_file, delete_file, DEFAULT_BUCKET_NAME

st.title("AWS S3 Automation")

bucket_name = st.text_input("S3 Bucket Name", value=DEFAULT_BUCKET_NAME)

s3_client = boto3.client('s3', region_name="ap-south-1")

def list_bucket_objects(bucket):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            return [obj['Key'] for obj in response['Contents']]
        else:
            return []
    except ClientError:
        return []

bucket_exists = False
try:
    s3_client.head_bucket(Bucket=bucket_name)
    bucket_exists = True
except ClientError:
    bucket_exists = False

st.markdown(f"### Bucket Status: {'Exists ✅' if bucket_exists else 'Does not exist ❌'}")

if st.button("Create Bucket", disabled=bucket_exists):
    success, msg = create_bucket(bucket_name)
    if success:
        st.success(msg)
    else:
        st.error(msg)

st.markdown("---")

with st.expander("Upload File"):
    upload_file_obj = st.file_uploader("Choose a file to upload")
    upload_btn_disabled = upload_file_obj is None or not bucket_exists
    if upload_file_obj:
        st.write(f"Filename: {upload_file_obj.name}, Size: {upload_file_obj.size/1024:.2f} KB")
    if st.button("Upload", disabled=upload_btn_disabled):
        temp_file_path = f"./{upload_file_obj.name}"
        with open(temp_file_path, "wb") as f:
            f.write(upload_file_obj.getbuffer())
        success, msg = upload_file(bucket_name, temp_file_path, upload_file_obj.name)
        os.remove(temp_file_path)
        if success:
            st.success(msg)
        else:
            st.error(msg)

with st.expander("Download File"):
    available_files = list_bucket_objects(bucket_name) if bucket_exists else []
    if available_files:
        download_key = st.selectbox("Select file to download", available_files)
        if st.button("Download", disabled=not bucket_exists or not download_key):
            success, msg = download_file(bucket_name, download_key, download_key)
            if success:
                st.success(msg)
            else:
                st.error(msg)
    else:
        st.info("No files available in the bucket for download.")

with st.expander("Delete File"):
    if bucket_exists:
        available_files = list_bucket_objects(bucket_name)
        if available_files:
            delete_key = st.selectbox("Select file to delete", available_files, key="delete_select")
            if st.button("Delete", disabled=not delete_key):
                success, msg = delete_file(bucket_name, delete_key)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
        else:
            st.info("No files available in the bucket to delete.")
    else:
        st.info("Bucket does not exist yet.")
