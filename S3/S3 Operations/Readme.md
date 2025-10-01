
---

# ☁️ AWS S3 Operations with Streamlit

A lightweight **Streamlit** web app to automate common **AWS S3** tasks—bucket creation, file upload, download, and deletion. Built with **Python** and **Boto3**, it uses your local AWS CLI credentials for seamless authentication and configuration.

---

## ✨ Features

- 🪣 Create an S3 bucket in the Asia Pacific (Mumbai) region (`ap-south-1`)  
- 📤 Upload files from your local machine to the S3 bucket  
- 📥 List and download files from the bucket to your working directory  
- 🗑️ Delete files from the bucket  
- 🖥️ Streamlit UI with real-time feedback and validation  

---

## 📝 Prerequisites

Before running the app, make sure you have:

- 🐍 Python 3.7+  
- 🔐 AWS CLI configured with appropriate permissions (`aws configure`)  
- 📦 Required Python packages installed:

```bash
pip install boto3 streamlit
```

---

## 📁 Project Structure

```
s3_automation/
├── s3_operations.py   # Core S3 helper functions (create, upload, download, delete)
├── app.py             # Streamlit app providing UI for S3 operations
└── README.md          # This documentation file
```

---

## 🚀 Usage

1. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

2. **Open the provided URL** in your browser (usually http://localhost:8501)

3. **Enter or confirm the bucket name** (default is `s3-ops`)

4. **Use the UI** to:
   - 🪣 Create a bucket  
   - 📤 Upload files  
   - 📥 Download files  
   - 🗑️ Delete files  

5. **Receive feedback** for each operation—success messages or error alerts

---

## 🧠 Notes

- 📂 Files are downloaded to the directory where you run `streamlit run app.py`  
- 🌍 Bucket names must be globally unique—update the default name in `s3_operations.py` if needed  
- 🔐 The app uses your local AWS CLI credentials—ensure your IAM user has the necessary S3 permissions  

---

