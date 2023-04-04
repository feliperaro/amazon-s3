import boto3


def download_file_bucket(bucket_name, file_name, file_path):
    print("download_file_bucket()")

    print(f"bucket_name: {bucket_name}. ")
    print(f"file_name: {file_name}. ")
    print(f"file_path: {file_path}. ")

    print("Connecting s3 client...")
    s3 = boto3.client('s3')

    print("Downloading file...")
    response = s3.download_file(Bucket=bucket_name, Key=file_name, Filename=file_path)

    print(f"response: {response}. ")
    return response



bucket_name = "new-bucket333"
# bucket_name = "YOUR_BUCKET_NAME"

file_name = "users.xlsx"
# file_name = "YOUR_FILE"

file_path = fr"C:\tmt\{file_name}"
# file_path = "YOUR_FILE"


download_file_bucket(bucket_name=bucket_name, file_name=file_name, file_path=file_path)


