import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    #When tag, value, children and props are the same the HTMLNode objects are equal
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)
        
    def test_tag(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("div", "This is a paragraph")
        self.assertNotEqual(node, node2)
        
    def test_value(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a different paragraph")
        self.assertNotEqual(node, node2)
        
    def test_children(self):
        node = HTMLNode("p", "This is a paragraph", [HTMLNode("p", "Child text")])
        node2 = HTMLNode("p", "This is a paragraph", [HTMLNode("em", "italic text")])
        self.assertNotEqual(node, node2)
        
    def test_props(self):
        node = HTMLNode("p", "This is a paragraph", props={"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a paragraph", props={"href": "https://www.yahoo.com"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", props={"href": "https://www.google.com", "class": "paragraph"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" class="paragraph"')



    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph")
        expected_repr = "HTMLNode(p, This is a paragraph, [], {})"
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here</a>')
 

    #testing parent node
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    
    def test_to_html_with_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_value(self):
        leaf_node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    
    #Testing text node to html node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    
    def test_bold_text(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "Bold text")


    def test_link_missing_url(self):
        node = TextNode("Click here", TextType.LINK)  # No URL provided
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    #Test for image
    def test_image_text_node(self):
        node = TextNode("An image", TextType.IMAGE, url="https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "An image"})


    def test_italic_text(self): 
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "Italic text")
        
if __name__ == "__main__":
    unittest.main()