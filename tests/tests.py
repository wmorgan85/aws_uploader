import os
import unittest
import filecmp
import warnings

# from progress import Progress
from upload.Uploader import Uploader


class TestUpload(unittest.TestCase):
    """
    Test cases for AWS connectivity
    """
    def setUp(self):
        filename = "sample_file.txt"
        test_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(test_dir, filename)
        warnings.simplefilter("ignore", ResourceWarning)
        u = Uploader(profile_name='wmorgan85')
        u.upload_file(filepath, "wmorgan85-iot-dashboard", filename)

    def tearDown(self):
        u = Uploader(profile_name='wmorgan85')
        u.delete_file("sample_file.txt", "wmorgan85-iot-dashboard")

    def test_can_create_s3_client_with_profile(self):
        u = Uploader()
        s = u.create_s3_client(profile_name='wmorgan85')
        self.assertIsNotNone(s)

    def test_can_list_s3_buckets(self):
        u = Uploader()
        bucket_list = u.list_buckets()
        is_list = isinstance(bucket_list, list)
        self.assertEqual(is_list, True)

    def test_can_list_bucket_items(self):
        u = Uploader()
        items = u.list_items("wmorgan85-iot-dashboard")
        validation_list = [
            "README",
            "index.html",
            "moviedata.json",
            "refresh.js",
            "requirements.txt",
            "sample_file.txt"
        ]
        self.assertEqual(items, validation_list)

    def test_can_upload_file(self):
        bucket = "wmorgan85-iot-dashboard"
        filename = "sample_file.txt"
        test_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(test_dir, filename)
        u = Uploader(profile_name='wmorgan85')
        self.assertEqual(u.upload_file(filepath, bucket, filename), True)

    def test_can_download_file(self):
        bucket = "wmorgan85-iot-dashboard"
        filename = "sample_file.txt"
        test_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(test_dir, filename)
        u = Uploader(profile_name='wmorgan85')
        u.download_file(filename, filepath+".new", bucket)
        self.assertEqual(filecmp.cmp(filepath, filepath+".new"), True)

    def test_can_delete_file(self):
        bucket = "wmorgan85-iot-dashboard"
        filename = "sample_file.txt"
        expected_response = [{'Key': filename}]
        u = Uploader(profile_name='wmorgan85')
        response = u.delete_file(filename, bucket)
        self.assertEqual(response, expected_response)

    # TODO - all of these...
    def test_can_create_s3_client_with_secrets(self):
        pass

    def test_can_close_s3_session(self):
        pass

    def test_can_send_file_with_permissions(self):
        pass

    def test_can_send_file_with_progress(self):
        pass


"""
class TestProgress(unittest.TestCase):
    def test_can_create_progress_counter(self):
        sample_file_name = "sample_file.txt"
        p = Progress(sample_file_name)
        self.assertEqual(p._size, float(os.path.getsize(sample_file_name)))
"""


if __name__ == "__main__":
    unittest.main()
