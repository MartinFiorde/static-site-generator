import re

from src.models.text_node import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
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
