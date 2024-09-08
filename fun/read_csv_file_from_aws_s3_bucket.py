import boto3


AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
AWS_S3_SIGNATURE_NAME = "s3v4",
AWS_S3_REGION_NAME = "us-east-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


s3_client = boto3.client(
    "s3",
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)


def read_file_from_s3(bucket_name, file_name):
    """Read and return content of a file stored in aws s3 bucket"""

    obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    data = obj['Body'].read()
    return data

r_file = read_file_from_s3(
    AWS_STORAGE_BUCKET_NAME, "file_name.csv"
)

f_decode = r_file.decode()

def delete_file():
    m_path = r_file.document

    if m_path:
        m_path.delete()

# for reading the csv header
splt_data = f_decode.split("\n")
