from enum import Enum

from src.models.leaf_node import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    BLOCK_CODE = "block_code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"


class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = self.validate_text_type(text_type)
        self.url = url

    def validate_text_type(self, text_type: str):
        # faster validation only if all Keys in enum match their value.upper() versions
        try:
            return TextType[text_type.upper()].value  # Convierte a mayúsculas y busca en el Enum
        except KeyError:
            raise ValueError(f"Invalid text_type: '{text_type}'. Allowed values are: {[t.name for t in TextType]}")
        
        # slight slower validation if not all Keys in enum match their value.upper() versions
        for t in TextType:
            if t.value == text_type:
                return t.value
        raise ValueError(
            f"Invalid text_type: '{text_type}'. Allowed values are: {[t.value for t in TextType]}"
        )

    def text_node_to_html_node(text_node: "TextNode") -> "LeafNode":
        type: TextType = text_node.text_type
        if type == TextType.TEXT.value:
            return LeafNode(text_node.text)
        elif type == TextType.BOLD.value:
            return LeafNode(text_node.text, "b")
        elif type == TextType.ITALIC.value:
            return LeafNode(text_node.text, "i")
        elif type == TextType.CODE.value:
            return LeafNode(text_node.text, "code")
        elif type == TextType.LINK.value:
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        elif type == TextType.IMAGE.value:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError("TextNode must have a valid TextType")

    def __eq__(self, other) -> bool:
        if isinstance(other, TextNode):
            return (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
        return False

    def __repr__(self) -> str:
        return f"TextNode(text={self.text!r}, text_type={self.text_type!r}, url={self.url!r})"

    def __str__(self):
        return f"<{self.text} - {self.text_type} - {self.url}>"
