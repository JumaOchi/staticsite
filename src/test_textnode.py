import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    #When url property is None
    def test_url_defaults_to_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)  # URL should be None by default


    #When text_type property is different the TestNode objects are not equal 
    def test_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

        
    #Different text content should result in inequality
    def test_different_text_not_equal(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)  # Different text should mean different objects
        

    #Different url content should result in inequality
    def test_different_urls_not_equal(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)  # Different URLs should make them different


    # Testing string representation of TextNode
    def test_repr(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        expected_repr = "TextNode(Click here, link, https://example.com)"
        self.assertEqual(repr(node), expected_repr)  # __repr__ should return the correct format
    

if __name__ == "__main__":
    unittest.main()