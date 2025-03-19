from unittest import TestCase
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(TestCase):
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
