import boto3
import logging

from botocore.exceptions import ClientError
from progress import ProgressPercentage


class Uploader(object):

    def create_s3_client(self, profile_name):
        """Create an s3 client

        """
        if profile_name is not None:
            session = boto3.Session(profile_name=profile_name)
        else:
            session = boto3.Session()
        return session.client("s3")

    def upload_file(self, file_name, bucket, object_name=None,
                    show_progress=False,
                    extraargs=None):
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

    def delete_file(self, filename, bucket):
        """Delete file from bucket
        :param filename: filename to delete
        :param bucket: bucket from which to delete
        :return: True if file was deleted else False
        """
        delete = {
            "Objects": [
                {
                    "Key": filename,
                    "VersionId": "null"
                }
            ]
        }
        delete["Objects"] = [{'Key': filename}]
        response = self.s3_client.delete_objects(Bucket=bucket, Delete=delete)
        return response['Deleted']

    def download_file(self, objectname, filename, bucket):
        with open(filename, 'wb') as f:
            self.s3_client.download_fileobj(bucket, objectname, f)
        return f

    def list_buckets(self):
        """List all S3 buckets in my profile"""

        session = boto3.Session(profile_name='wmorgan85')
        dev_s3_client = session.client('s3')
        response = dev_s3_client.list_buckets()
        return response["Buckets"]

    def list_items(self, bucketname):
        items = []
        response = self.s3_client.list_objects_v2(Bucket=bucketname)
        for item in response['Contents']:
            items.append(item['Key'])
        return items

    def run_examples(self):
        print("*****Listing buckets example...")
        self.list_buckets()
        print("*****Uploading small file example...")
        self.upload_file("README", "wmorgan85-iot-dashboard")
        print("*****Uploading big file example...")
        self.upload_file(
            "moviedata.json",
            "wmorgan85-iot-dashboard",
            show_progress=True
        )

    def __init__(self, profile_name=None):
        self.s3_client = self.create_s3_client(profile_name)


if __name__ == "__main__":
    uploader = Uploader()
    uploader.run_examples()
