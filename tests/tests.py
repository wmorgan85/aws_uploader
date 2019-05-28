import boto3
import os
import unittest

# from progress import Progress
from upload import upload


class TestUpload(unittest.TestCase):
    """
    Test cases for AWS connectivity
    """
    def test_can_open_close_s3_session(self):
        session = boto3.Session(profile_name='wmorgan85')
        print(session.profile_name)

    def test_can_close_s3_session(self):
        pass

    def test_can_send_simple_file(self):
        bucket = "wmorgan85-iot-dashboard"
        test_dir = os.path.dirname(os.path.realpath(__file__))
        filename = "sample_file.txt"
        filename = os.path.join(test_dir, filename)
        self.assertEqual(upload.upload_file(filename, bucket), True)

    def test_can_send_file_with_permissions(self):
        pass

    def test_can_send_file_with_progress(self):
        pass

    def test_can_download_file(self):
        pass

    def test_can_delete_file(self):
        pass

    def test_can_list_s3_buckets(self):
        bucket_list = upload.list_buckets()
        self.assertEqual(type(bucket_list), type(list()))


"""
class TestProgress(unittest.TestCase):
    def test_can_create_progress_counter(self):
        sample_file_name = "sample_file.txt"
        p = Progress(sample_file_name)
        self.assertEqual(p._size, float(os.path.getsize(sample_file_name)))
"""


if __name__ == "__main__":
    unittest.main()
