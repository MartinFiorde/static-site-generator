import re

from src.models.text_node import TextNode, TextType


def nodify(text: str):
    if not isinstance(text, str):
        raise TypeError("Parameter must be a valid string.")
    if text == "":
        return []
    return [TextNode(text, TextType.TEXT)]


def pick_delimiter(text_type):
    if text_type == TextType.BOLD:
        return "**"
    if text_type == TextType.ITALIC:
        return "*"
    if text_type == TextType.CODE:
        return "`"
    return None


def split_nodes_delimiter(text: str, text_type: TextType) -> list[TextNode]:
    return split_nodes_delimiter(nodify(text), text_type)


def split_nodes_delimiter(
    old_nodes: list[TextNode], text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        delimiter = pick_delimiter(text_type)
        segments = old_node.text.split(delimiter)
        if len(segments) % 2 == 0:
            raise Exception(
                "Invalid Markdown syntax, one closing delimiter is missing."
            )
        for segment in segments:
            if segment == "":
                continue
            if segments.index(segment) % 2 == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                new_nodes.append(TextNode(segment, text_type))
    return new_nodes


def pattern_selector(text_type: TextType) -> str:
    if text_type == TextType.LINK:
        return r"(\[.*?\]\(.*?\))"
    elif text_type == TextType.IMAGE:
        return r"(!\[.*?\]\(.*?\))"
    else:
        raise TypeError("TextType invalid.")


def split_nodes_with_url(
    old_nodes: list[TextNode], text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        pattern = pattern_selector(text_type)
        segments = re.split(pattern, old_node.text)
        # delimiter = pick_delimiter(text_type)
        # segments = old_node.text.split(delimiter)
        if len(segments) % 2 == 0:
            raise Exception(
                "Invalid Markdown syntax, one closing delimiter is missing."
            )
        for segment in segments:
            if segment == "":
                continue
            if segments.index(segment) % 2 == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                text = re.search(r"\[(.*?)\]", segment).group(1)
                url = re.search(r"\((.*?)\)", segment).group(1)
                new_nodes.append(TextNode(text, text_type, url))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = nodify(text)
    nodes = split_nodes_delimiter(nodes, TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, TextType.CODE)
    nodes = split_nodes_with_url(nodes, TextType.IMAGE)
    nodes = split_nodes_with_url(nodes, TextType.LINK)
    return nodes


def markdown_to_blocks(markdown: str) -> list[str]:
    nodes = []

    temp_flag = None
    temp_block = []
    for segment in markdown.split("\n"):
        line = segment.strip()

        if temp_flag == "```":
            temp_block.append(segment)
            if line[:3] == "```":
                temp_block[-1] = line
                nodes.append("\n".join(temp_block))
                temp_flag = None
                temp_block = []
            continue

        if line == "":
            continue

        if temp_flag != None:
            if temp_flag == line[: len(temp_flag)]:
                temp_block.append(line)
                continue

            if re.match(r"^\d+\.\s", temp_flag) and re.match(r"^\d+\.\s", line):
                temp_block.append(line)
                continue

            nodes.append("\n".join(temp_block))
            temp_flag = None
            temp_block = []

        if re.match(r"^#{1,6} ", line):
            nodes.append(line)
            continue

        if re.match(r"^\*\s", line):
            temp_flag = "* "
            temp_block.append(line)
            continue

        if re.match(r"^\-\s", line):
            temp_flag = "- "
            temp_block.append(line)
            continue
        
        if re.match(r"^\>\s", line):
            temp_flag = "> "
            temp_block.append(line)
            continue

        if line == "```":
            temp_flag = line
            temp_block.append(line)
            continue

        nodes.append(line)

    if len(temp_block) != 0:
        if temp_flag == "```":
            temp_block.append(temp_flag)
        nodes.append("\n".join(temp_block))
    
    return nodes
