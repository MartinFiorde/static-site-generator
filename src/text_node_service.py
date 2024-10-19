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


def split_nodes_delimiter(data: list[TextNode], text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in data:
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


"""
def text_to_textnodes(text):
    nodes = split_nodes_delimiter(text, "**", TextType.BOLD)
    nodes = nodes[:-1] + split_nodes_delimiter(
        nodes[len(nodes) - 1].text, "*", TextType.ITALIC
    )
    nodes = nodes[:-1] + split_nodes_delimiter(
        nodes[len(nodes) - 1].text, "`", TextType.CODE
    )
    nodes = nodes[:-1] + split_nodes_delimiter(
        nodes[len(nodes) - 1].text, None, TextType.IMAGE
    )
    nodes = nodes[:-1] + split_nodes_delimiter(
        nodes[len(nodes) - 1].text, None, TextType.LINK
    )
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    if text_type == TextType.LINK:
        return link_procesor(old_nodes)
    if text_type == TextType.IMAGE:
        return image_procesor(old_nodes)

    items = old_nodes.split(delimiter, 2)

    if len(items) != 3:
        return [TextNode(old_nodes, TextType.TEXT)]

    result: list = []
    for item in items:
        if item == "":
            continue
        if item == items[0]:
            result.append(TextNode(item, TextType.TEXT))
        if item == items[1]:
            result.append(TextNode(item, text_type))
        if item == items[2]:
            result = result + split_nodes_delimiter(item, delimiter, text_type)
    return result


def link_procesor(old_nodes) -> list[TextNode]:
    parts = re.split(r"\[.*?\]\([^\)]+\)", old_nodes, 1)

    if len(parts) != 2:
        return [TextNode(old_nodes, TextType.TEXT)]

    head = parts[0]
    tail = parts[1]
    result: list = []
    if head != "":
        result.append(TextNode(head, TextType.TEXT))

    text = re.search(r"\[(.*?)\]", old_nodes)
    url = re.search(r"\((.*?)\)", old_nodes)
    if not text or not url:
        raise ValueError("Link markdown format is invalid")
    result.append(TextNode(text.group(1), TextType.LINK, url.group(1)))

    if tail != "":
        result = result + split_nodes_delimiter(tail, None, TextType.LINK)

    return result


def image_procesor(old_nodes) -> list[TextNode]:
    parts = re.split(r"!\[.*?\]\([^\)]+\)", old_nodes, 1)

    if len(parts) != 2:
        return [TextNode(old_nodes, TextType.TEXT)]

    head = parts[0]
    tail = parts[1]
    result: list = []
    if head != "":
        result.append(TextNode(head, TextType.TEXT))

    text = re.search(r"\!\[(.*?)\]", old_nodes)
    url = re.search(r"\((.*?)\)", old_nodes)
    if not text or not url:
        raise ValueError("Image markdown format is invalid")
    result.append(TextNode(text.group(1), TextType.IMAGE, url.group(1)))

    if tail != "":
        result = result + split_nodes_delimiter(tail, None, TextType.IMAGE)

    return result
"""
