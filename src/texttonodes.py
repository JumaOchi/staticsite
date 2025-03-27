from textnode import TextNode, TextType
import re

from splitdelimiter import split_nodes_delimiter
from extractlink import split_nodes_image, split_nodes_link
#This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

def text_to_textnodes(text) :
    # we start with bold italic and code for a start
    
    nodes = [TextNode(text, TextType.TEXT)]

    #Processing inline elements in order
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

      # Step 3: Process images
    nodes = split_nodes_image(nodes)

    # Step 4: Process links
    nodes = split_nodes_link(nodes)

       # Debugging
    #print("Processed nodes:", nodes)  # See if images were properly detected
    return nodes

