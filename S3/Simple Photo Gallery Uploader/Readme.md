
---

# 📸 Simple Photo Gallery Uploader

A **Streamlit** web application that allows users to upload photos to an **AWS S3** bucket. Uploaded images are displayed in a neat gallery with temporary public access via pre-signed URLs.

---

## ✨ Features

- 🖼️ Upload multiple image files at once  
- ☁️ Store images in an AWS S3 bucket (`uploads/` prefix)  
- 🔐 Generate temporary, secure public access via **pre-signed URLs**  
- 🖼️ View uploaded images in a gallery inside the app  
- 🎨 Clean, user-friendly interface (upload via sidebar, gallery in main view)  
- ✅ Upload success notifications and graceful error handling  

---

## 🛠 Technologies Used

- 🐍 Python 3.x  
- 🌐 [Streamlit](https://streamlit.io/) for UI  
- ☁️ [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for AWS S3 integration  
- 📦 AWS S3 for object storage  

---

## 📝 Prerequisites

Before you begin, make sure you have the following:

- 🔑 AWS account with an **S3 bucket** created  
- 🔐 AWS credentials configured locally (`~/.aws/credentials`) or via environment variables  
- 🐍 Python 3.x installed  
- 📦 Required Python packages (see **Installation** section)  

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/photo-gallery-uploader.git
cd photo-gallery-uploader
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes:

```
streamlit
boto3
```

### 3. Configure AWS credentials

You can configure them using the AWS CLI:

```bash
aws configure
```

Or manually set environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=ap-south-1
```

### 4. Update the S3 bucket name

Open `app.py` and update the `S3_BUCKET` variable with your bucket name.  
Alternatively, modify the code to read the bucket name from an environment variable.

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the URL displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)) in your browser.

---

## 📂 Uploading and Viewing

- Use the sidebar to select and upload image files  
- Uploaded images will appear in the main gallery view, along with their filenames  

---

## ⭐ Contributing

Feel free to star ⭐ the repository and contribute to this project via issues or pull requests. Contributions are welcome! 🚀

---


