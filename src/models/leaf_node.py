from src.models.html_node import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def to_html(self, tab=0):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return f"{'    '*tab}{self.value}"
        
        return f"{'    '*tab}<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        return False

    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"

