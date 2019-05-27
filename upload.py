import boto3
import logging

from botocore.exceptions import ClientError
from progress import ProgressPercentage


def upload_file(file_name, bucket, object_name=None, show_progress=False):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Target bucket
    :param object_name: S3 object name. If not specified file_name is used
    :return: True if file was uploaded else False
    """

    # if the s3 object name wasn't specified use the file name
    if object_name is None:
        object_name = file_name

    session = boto3.Session(profile_name='wmorgan85')
    s3_client = session.client('s3')
    try:
        if show_progress:
            s3_client.upload_file(
                file_name, bucket, object_name,
                Callback=ProgressPercentage(file_name),
                ExtraArgs={'ACL': 'public-read'}
            )
        else:
            s3_client.upload_file(
                file_name, bucket, object_name,
                ExtraArgs={'ACL': 'public-read'}
            )
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_buckets():
    """List all S3 buckets in my profile"""

    session = boto3.Session(profile_name='wmorgan85')

    dev_s3_client = session.client('s3')

    response = dev_s3_client.list_buckets()

    # print out the bucket names
    for bucket in response["Buckets"]:
        print(bucket["Name"])


def run_examples():
    print("*****Listing buckets example...")
    list_buckets()
    print("*****Uploading small file example...")
    upload_file("README", "wmorgan85-iot-dashboard")
    print("*****Uploading big file example...")
    upload_file(
        "moviedata.json",
        "wmorgan85-iot-dashboard",
        show_progress=True
    )


if __name__ == "__main__":
    run_examples()
