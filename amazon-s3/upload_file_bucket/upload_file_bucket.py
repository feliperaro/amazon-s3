import boto3


def upload_file_bucket(bucket_name, file_name, file_path):
    print("upload_file_bucket()")

    print(f"bucket_name: {bucket_name}. ")
    print(f"file_name: {file_name}. ")
    print(f"file_path: {file_path}. ")

    print("Connecting s3 client...")
    s3 = boto3.client('s3')

    print("Uploading file to bucket...")
    response = s3.upload_file(file_path, bucket_name, file_name)

    print(f"response: {response}. ")
    return response


def download_file_bucket(bucket_name, file_name, file_path):
    print("download_file_bucket()")

    print(f"bucket_name: {bucket_name}. ")
    print(f"file_name: {file_name}. ")
    print(f"file_path: {file_path}. ")

    print("Connecting s3 client...")
    s3 = boto3.client('s3')

    response = s3.download_file(Bucket=bucket_name, Key=file_name, Filename=file_path)
    print(f"response: {response}. ")
    return response



bucket_name = "new-bucket333"
# bucket_name = "YOUR_BUCKET_NAME"

file_name = "users.xlsx"
# file_name = "YOUR_FILE"

file_path = fr"C:\tmt\{file_name}"
# file_path = "YOUR_FILE"


# upload_file_bucket(bucket_name=bucket_name, file_name=file_name, file_path=file_path)
download_file_bucket(bucket_name=bucket_name, file_name=file_name, file_path=file_path)