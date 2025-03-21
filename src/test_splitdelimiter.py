import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    
    def test_split_normal_text(self):
        """Test splitting normal text with backticks for code blocks."""
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_bold_text(self):
        """Test splitting bold text with double asterisks for bold formatting."""
        node = TextNode("This is **bold text** inside", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" inside", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_italic_text(self):
        """Test splitting italic text with underscores."""
        node = TextNode("Some _italicized_ words", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected_nodes = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" words", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_no_matching_delimiter_raises_error(self):
        """Test when there is an opening delimiter but no closing delimiter."""
        node = TextNode("This is `unmatched code block", TextType.NORMAL)
        
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(context.exception), "Invalid Markdown: Unmatched delimiter '`' found in text.")

    def test_non_text_nodes_remain_unchanged(self):
        """Test that non-text nodes like images and links are not split."""
        node = TextNode("https://example.com/image.png", TextType.IMAGE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [node])  # Image should remain unchanged

if __name__ == "__main__":
    unittest.main()
