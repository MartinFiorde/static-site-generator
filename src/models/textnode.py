class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
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
        return f"<{self.text} {self.text_type} {self.url}>"

