from src.models.html_node import HTMLNode
from src.models.text_node import TextNode, TextType


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self, tab=0):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return f"{'    '*tab}{self.value}"
        
        return f"{'    '*tab}<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def text_node_to_html_node(text_node: TextNode) -> 'LeafNode':
        type: TextType = text_node.text_type
        if type == TextType.TEXT:
            return LeafNode(text_node.text)
        elif type == TextType.BOLD:
            return LeafNode(text_node.text, "b")
        elif type == TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        elif type == TextType.CODE:
            return LeafNode(text_node.text, "code")
        elif type == TextType.LINK:
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        elif type == TextType.IMAGE:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError("TextNode must have a valid TextType")


    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        return False

    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"

