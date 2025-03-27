from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    """Extracts markdown-style image references, supporting both absolute and relative URLs."""
    return re.findall(r"!\[(.+?)\]\(([^)]+)\)", text)

def extract_markdown_links(text):
    """Extracts markdown-style links from text, supporting both absolute and relative URLs."""
    return re.findall(r"(?<!!)\[(.+?)\]\(([^)\s]+)\)", text)


def split_nodes_image(old_nodes):
    """Splits text nodes containing markdown images into separate TextNode instances."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(node)
            continue

        for alt_text, img_url in matches:
            split_text = text.split(f"![{alt_text}]({img_url})", 1)
            
            if split_text[0]:  # Add text before the image
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            print(f"Creating image node: alt={alt_text}, url={img_url}")
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))  # Store img URL in `url`


            
            text = split_text[1] if len(split_text) > 1 else ""
        
        if text:  # Add remaining text after last image
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    """Splits text nodes containing markdown links into separate TextNode instances."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:  # FIXED: Used TEXT instead of NORMAL
            new_nodes.append(node)
            continue
        
        text = node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            continue

        for link_text, link_url in matches:
            split_text = text.split(f"[{link_text}]({link_url})", 1)

            if split_text[0]:  # Add text before the link
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            text = split_text[1] if len(split_text) > 1 else ""

        if text:  # Add remaining text after last link
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes



        