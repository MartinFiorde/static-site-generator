import re

from src.models.text_node import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    if text_type == TextType.LINK:
        return link_procesor(old_nodes)
    if text_type == TextType.IMAGE:
        return image_procesor(old_nodes)

    items = old_nodes.split(delimiter)
    result: list = []
    for item in items:
        if item == "":
            continue

        if len(items) == 3 and item == items[1]:
            result.append(TextNode(item, text_type))
        else:
            result.append(TextNode(item, TextType.TEXT))
    return result


def link_procesor(old_nodes) -> list[TextNode]:
    parts = re.split(r"\[.*?\]\(.*?\)", old_nodes)
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
        result.append(TextNode(tail, TextType.TEXT))

    return result


def image_procesor(old_nodes) -> list[TextNode]:
    parts = re.split(r"\!\[.*?\]\(.*?\)", old_nodes)
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
        result.append(TextNode(tail, TextType.TEXT))

    return result
