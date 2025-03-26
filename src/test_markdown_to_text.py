import unittest
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
import textwrap
class TestMarkdown_To_Blocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = textwrap.dedent("""\
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
            """)  # Remove extra spaces from indentation
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_line_markdown(self):
        md = "Just a single line of text."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single line of text."])


    def test_multiple_consecutive_newlines(self):
        md = textwrap.dedent("""\
            First paragraph.


            Second paragraph after multiple newlines.

            - Item 1
            - Item 2
        """)
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph after multiple newlines.",
                "- Item 1\n- Item 2",
            ],
        )

    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```code```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote\n> look\n> Bitch"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. List item\n2. Item two\n3. Item 3"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(""), None)
        self.assertNotEqual(block_to_block_type("1. Will\n3. Fucking Power\n4. We win"), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()