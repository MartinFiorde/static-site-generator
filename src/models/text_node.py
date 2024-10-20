from enum import Enum


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
    def __init__(self, text: str, text_type: TextType, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

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
