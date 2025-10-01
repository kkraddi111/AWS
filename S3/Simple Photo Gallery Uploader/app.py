
import streamlit as st
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

S3_BUCKET = "s3photo-gallery"

s3_client = boto3.client(
    's3',
    region_name='ap-south-1',
    config=Config(signature_version='s3v4', s3={'addressing_style': 'virtual'})
)


def upload_file_to_s3(file_obj, bucket, key):
    try:
        s3_client.upload_fileobj(file_obj, bucket, key)
        return True
    except ClientError as e:
        st.error(f"S3 upload failed: {e}")
        return False


def generate_presigned_url(bucket, key, expiration=3600):
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=expiration
        )
        url = url.replace('s3.amazonaws.com', 's3.ap-south-1.amazonaws.com')
        return url
    except ClientError as e:
        st.error(f"Failed to generate pre-signed URL: {e}")
        return None


def initialize_session_state():
    if 'uploaded_images' not in st.session_state:
        st.session_state.uploaded_images = []


def handle_upload(files):
    success_count = 0
    fail_count = 0
    for file in files:
        key = f"uploads/{file.name}"
        if upload_file_to_s3(file, S3_BUCKET, key):
            url = generate_presigned_url(S3_BUCKET, key)
            if url:
                st.session_state.uploaded_images.append({'key': key, 'url': url, 'name': file.name})
                success_count += 1
            else:
                fail_count += 1
        else:
            fail_count += 1
    if success_count > 0:
        st.success(f"Uploaded {success_count} file(s) successfully!")
    if fail_count > 0:
        st.error(f"Failed to upload {fail_count} file(s).")


def render_gallery():
    st.markdown("## Uploaded Photos Gallery")
    images = st.session_state.uploaded_images
    if images:
        cols_per_row = 3
        for i in range(0, len(images), cols_per_row):
            cols = st.columns(cols_per_row)
            for col, img in zip(cols, images[i:i+cols_per_row]):
                with col:
                    st.image(img['url'], use_container_width=True)
                    st.caption(img.get('name', img.get('key', 'Unnamed')))
    else:
        st.info("No images uploaded yet.")



def main():
    st.title("📸 Simple Photo Gallery Uploader")

    initialize_session_state()

    with st.sidebar:
        st.header("Upload Images")
        uploaded_files = st.file_uploader(
            "Select image(s) to upload",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
            accept_multiple_files=True
        )
        if uploaded_files and st.button("Upload"):
            handle_upload(uploaded_files)

    st.markdown("---")
    render_gallery()


if __name__ == "__main__":
    main()
