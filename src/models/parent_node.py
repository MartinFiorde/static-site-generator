from src.models.html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self, tab=0):
        if self.children == None or len(self.children) == 0:
            raise ValueError("All leaf nodes must have at least one children")

        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")

        full_node = f"{'    '*0}<{self.tag}{self.props_to_html()}>"
        for item in self.children:
            if self.tag == "pre":
                full_node += f"{item.to_html(0)}"
            else:
                full_node += f"{item.to_html(0)}"
        if self.tag == "pre":
            full_node += f"{'    '*0}</{self.tag}>"
        else:
            full_node += f"{'    '*0}</{self.tag}>"
        return full_node

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
            )
        return False

    def __repr__(self):
        return (
            f"ParentNode(tag={self.tag!r}, children={self.children!r}, props={self.props!r})"
        )
