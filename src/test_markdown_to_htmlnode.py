import unittest
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import ParentNode, HTMLNode, LeafNode


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <strong>bolded</strong> paragraph text in a p tag here</p><p>This is another paragraph with <em>italic</em> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff 
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        markdown = """1. First item
    2. Second item
    3. Third item"""
        
        expected_html = """<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"""
        
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected_html)


    def test_unordered_list(self):
        markdown = """- Item one
    - Item two
    - Item three"""
        
        expected_html = """<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>"""
        
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()