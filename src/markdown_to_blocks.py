from textnode import TextNode, TextType
from enum import Enum
import re

def markdown_to_blocks(markdown) :
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if block == "":
        return None
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(re.match(r"^> ", line) for line in lines):
        return BlockType.QUOTE
    # Every line in unordered list starts with '- ', '* ', or '+ '
    if all(re.match(r"^\s*[-*+] ", line) for line in lines):
        return BlockType.UNORDERED_LIST
     # Extract numbers and check if they form a valid sequence (1., 2., 3., etc.)
    numbers = [int(re.match(r"^(\d+)\. ", line).group(1)) for line in lines if re.match(r"^\d+\.", line)]
    if numbers and numbers == list(range(1, len(numbers) + 1)):  # Ensure strict sequence
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH



    



