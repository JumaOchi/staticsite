from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type not in {TextType.NORMAL, TextType.BOLD, TextType.ITALIC}:
            new_nodes.append(node)  # Keep non-text nodes unchanged
            continue
        
        parts = node.text.split(delimiter)  # Split text by delimiter

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown: Unmatched delimiter '{delimiter}' found in text.")

        temp_nodes = []
        for i, part in enumerate(parts):
            new_type = text_type if i % 2 else node.text_type  # Use the same type for non-delimited text
            if part:  # Avoid adding empty strings
                temp_nodes.append(TextNode(part, new_type))

        new_nodes.extend(temp_nodes)  # Append processed nodes

    return new_nodes
