import re

from src.models.text_node import TextNode, TextType, BlockType
from src.models.parent_node import ParentNode
from src.models.leaf_node import LeafNode

from src.text_node_service import (
    text_to_textnodes,
    markdown_to_blocks,
    block_to_block_type,
)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        child_nodes.append(turn_block_into_node(block))
    return ParentNode("div", child_nodes)


def turn_block_into_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.BLOCK_CODE:
        return generate_block_code_node(block)
    if block_type == BlockType.HEADING:
        return generate_heading_node(block)
    if block_type == BlockType.PARAGRAPH:
        return generate_paragraph_node(block)
    if block_type == BlockType.QUOTE:
        return generate_quote_node(block)
    if block_type == BlockType.U_LIST:
        return generate_u_list_node(block)
    if block_type == BlockType.O_LIST:
        return generate_o_list_node(block)


def generate_block_code_node(block: str):
    lines = block.split("\n")
    if len(lines) < 2:
        raise Exception("block should had at least 3 lines")
    value = "\n" + "\n".join(lines[1:-1]) + "\n"
    leaf_nodes = [LeafNode(tag="code", value=value)]
    return ParentNode("pre", leaf_nodes)


def generate_heading_node(line: str):
    if len(line.split("\n")) > 1:
        raise Exception("block should be 1 single line")
    pair = line.split(" ", 1)
    tag = f"h{pair[0].count('#')}"
    text_nodes = text_to_textnodes(pair[1].strip())
    leaf_nodes = textnodes_to_leafnodes(text_nodes)
    return ParentNode(tag, leaf_nodes)


def generate_paragraph_node(line: str):
    if len(line.split("\n")) > 1:
        raise Exception("block should be 1 single line")
    text_nodes = text_to_textnodes(line)
    leaf_nodes = textnodes_to_leafnodes(text_nodes)
    return ParentNode("p", leaf_nodes)


def generate_quote_node(block: str):
    pass


def generate_u_list_node(block: str):
    pass


def generate_o_list_node(block: str):
    pass


def textnodes_to_leafnodes(text_nodes: list[TextNode]) -> list[LeafNode]:
    leaf_nodes = []
    for item in text_nodes:
        leaf_nodes.append(item.text_node_to_html_node())
    return leaf_nodes
