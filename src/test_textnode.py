import unittest

from textnode import TextNode, TextType
from extractlink import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
        node2 = TextNode("This is a text node", TextType.TEXT)
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
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)


    def test_extract_multiple_markdown_images_and_links(self):
        text = (
            "Here is an ![image1](https://i.imgur.com/abc.png) and "
            "another ![image2](https://i.imgur.com/xyz.jpg). "
            "Also, check [Google](https://google.com) and "
            "[OpenAI](https://openai.com)!"
        )

        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/abc.png"),
                ("image2", "https://i.imgur.com/xyz.jpg"),
            ],
            image_matches,
        )

        self.assertListEqual(
            [
                ("Google", "https://google.com"),
                ("OpenAI", "https://openai.com"),
            ],
            link_matches,
        )


    #Testing split nodes link and images

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ], new_nodes,
        )

        


if __name__ == "__main__":
    unittest.main()