import unittest
from textnode import TextNode, TextType
from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# This is the title"
        self.assertEqual(extract_title(md), "This is the title")

    def test_no_title(self):
        md = "This is not a title"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_empty_string(self):
        md = ""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()