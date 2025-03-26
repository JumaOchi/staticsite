from textnode import TextType, TextNode
from enum import Enum

class HtmlType(Enum):
    DIV = "div"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    CODE = "code"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"
    LIST_ITEM = "li"
    QUOTE = "blockquote"
    IMAGE = "img"
    LINK = "a"
    BOLD = "strong"
    ITALIC = "em"
    PARAGRAPH = "p"
    SPAN = "span"
    PRE = "pre"


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None): 
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def to_html(self):
        raise NotImplementedError
    
    
    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props =None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value  # Just return the text if there's no HTML tag
        
        tag_str = self.tag.value if isinstance(self.tag, HtmlType) else str(self.tag)  # Ensure string tag
        #print(f"Tag: {self.tag}, Type: {type(self.tag)}")  # Debugging statement
        return f"<{tag_str}{self.props_to_html()}>{self.value}</{tag_str}>"

        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")
        tag_str = self.tag.value if isinstance(self.tag, HtmlType) else str(self.tag)
        # Simply join children without adding extra spaces here.
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{tag_str}{self.props_to_html()}>{children_html}</{tag_str}>"


    
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode object")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("strong", text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("em", text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        # Detect block-level code (if it contains newlines, treat it as a block)
        if "\n" in text_node.text:
            return ParentNode("pre", [LeafNode("code", text_node.text)])
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("TextNode of type LINK must have a URL")
        return LeafNode("a", text_node.text, props={"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("TextNode of type IMAGE must have a URL")
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"Unsupported text type: {text_node.text_type}")

"""
# converting TextNode to an HTMLNode
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode) :
        raise TypeError("Expected a TextNode object")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("strong", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("em", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        # Ensure the URL is provided
        if not text_node.url:
            raise ValueError("TextNode of type LINK must have a URL")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        # Ensure the URL is provided
        if not text_node.url:
            raise ValueError("TextNode of type IMAGE must have a URL")
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})

    
    # Catch-all for unsupported types
    raise ValueError(f"Unsupported text type: {text_node.text_type}")"""
