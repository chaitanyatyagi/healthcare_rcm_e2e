from google.cloud import storage
import os


def upload_file(bucket, local_file_path, gcs_file_path):
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded {local_file_path} to gs://{bucket.name}/{gcs_file_path}")  

if __name__ == "__main__":
    bucket_name = "healthcare-rcm-d"
    dir_path = [
    os.path.abspath("/Users/root1/Development/data engineering/project/healthcare-e2e-rcm/data/EMR/hospital-a"),
    os.path.abspath("/Users/root1/Development/data engineering/project/healthcare-e2e-rcm/data/EMR/hospital-b")
    ]
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    for path in dir_path:
        hospital_name = path.split("/")[-1]
        for file in os.listdir(path):
            gcs_file_path = f"data/EMR/{hospital_name}/{file}"
            if file.endswith(".csv"):
                local_file_path = os.path.join(path,file)
                upload_file(bucket,local_file_path,gcs_file_path)
