from textnode import TextNode, TextType
from htmlnode import HTMLNode, HtmlType, ParentNode, LeafNode, text_node_to_html_node
from splitdelimiter import split_nodes_delimiter
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
import re
from texttonodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []  # Store all the processed block nodes

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            # Normalize whitespace: replace all whitespace runs with a single space, then trim.
            cleaned_text = re.sub(r'\s+', ' ', block).strip()
            children.append(ParentNode(HtmlType.PARAGRAPH, text_to_children(cleaned_text)))

        elif block_type == BlockType.HEADING:
            heading_level = len(re.match(r"^(#{1,6}) ", block).group(1))  # Count # symbols
            children.append(ParentNode(getattr(HtmlType, f"H{heading_level}"), text_to_children(block.lstrip("# "))))
        
        elif block_type == BlockType.IMAGE:
            children.append(text_node_to_html_node(text_to_textnodes(block)[0]))  # Only one image node
            
        elif block_type == BlockType.CODE:
            code_lines = block.split("\n")[1:-1]  # Remove the first and last triple backticks
            cleaned_code = "\n".join(line.lstrip() for line in code_lines).rstrip() + "\n"  # Remove leading spaces
            code_node = TextNode(cleaned_code, TextType.CODE)
            children.append(text_node_to_html_node(code_node))

        elif block_type == BlockType.QUOTE:
            children.append(ParentNode(HtmlType.QUOTE, text_to_children(block.lstrip("> "))))

        elif block_type == BlockType.UNORDERED_LIST:
            list_items = [re.sub(r"^\s*[-*+] ", "", item).strip() for item in block.split("\n") if item]
            list_nodes = [ParentNode(HtmlType.LIST_ITEM, text_to_children(item)) for item in list_items]
            children.append(ParentNode(HtmlType.UNORDERED_LIST, list_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            list_items = [re.sub(r"^\s*\d+\.\s*", "", item).strip() for item in block.split("\n") if item]
            list_nodes = [ParentNode(HtmlType.LIST_ITEM, text_to_children(item)) for item in list_items]
            children.append(ParentNode(HtmlType.ORDERED_LIST, list_nodes))


    return ParentNode(HtmlType.DIV, children)  # Wrap everything inside a div

# Convert a text string to a list of TextNodes
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for i, text_node in enumerate(text_nodes):
        node = text_node_to_html_node(text_node)
        # Insert a space node between adjacent inline nodes only if needed.
        if html_nodes:
            prev = html_nodes[-1]
            # Get rendered text of previous and current nodes.
            prev_text = prev.to_html() if hasattr(prev, 'to_html') else ""
            curr_text = node.to_html() if hasattr(node, 'to_html') else ""
            # If the previous output does not end with a space and current does not start with a space, insert one.
            if not prev_text.endswith(" ") and not curr_text.startswith(" "):
                html_nodes.append(LeafNode(None, " "))
        html_nodes.append(node)
    return html_nodes



