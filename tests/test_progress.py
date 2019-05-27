import boto3
import unittest
import os

from progress import Progress


class AwsTest(unittest.TestCase):
    """
    Test cases for AWS connectivity
    """
    def test_can_create_s3_session(self):
        session = boto3.Session(profile_name='wmorgan85')
        print(session.profile_name)

    def test_can_send_simple_file(self):
        pass

    def test_can_send_file_with_permissions(self):
        pass

    def test_can_send_file_with_progress(self):
        pass


class ProgressTest(unittest.TestCase):
    """
    Test cases for the Progress bar
    """
    def test_can_create_progress_counter(self):
        sample_file_name = "sample_file.txt"
        p = Progress(sample_file_name)
        self.assertEqual(p._size, float(os.path.getsize(sample_file_name)))
