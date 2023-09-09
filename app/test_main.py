from main import reversed_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def test_rev_str(self):
        random_string="hello world"
        string_reversed = "dlrow olleh"
        self.assertEqual(string_reversed,reversed_string(random_string))

    def test_get_env(self):
        self.assertEqual(os.environ.get('MODE'), get_mode())


if __name__ == '__main__':
    unittest.main()