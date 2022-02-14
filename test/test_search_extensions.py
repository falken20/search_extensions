from distutils import extension
from main import count_files, get_params
import unittest

class TestSearchExtensions (unittest.TestCase):
    
    def test_count_files_no_path(self):
        self.assertEqual(count_files(""), [])

    def test_count_files_err_path(self):
        self.assertEqual(count_files("/no_path"), [])

    def test_count_files_root_path(self):
        # self.assertTrue(len(count_files("/")) > 0)
        pass

    def test_get_params(self):
        path, extensions, files = get_params()
        self.assertIsInstance(path, str)
        self.assertIsInstance(extensions, str)
        self.assertIsInstance(files, list)


if __name__ == '__main__':
    unittest.main()
