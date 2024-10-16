import unittest

from src.models.parent_node import ParentNode
from src.models.leaf_node import LeafNode


class TestParentNode(unittest.TestCase):
    base_node = ParentNode(
        "p",
        [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text", None),
            LeafNode("italic text", "i"),
            LeafNode("Normal text", None),
        ],
        {"class": "greeting", "href": "https://boot.dev"},
    )
    node_with_extra_parent = ParentNode(
        "div",
        [
            ParentNode(
                "p",
                [
                    LeafNode("Bold text", "b"),
                    LeafNode("Normal text", None),
                    LeafNode("italic text", "i"),
                    LeafNode("Normal text", None),
                ],
            ),
            LeafNode(
                "Normal text",
                "a",
                {"class": "greeting", "href": "https://boot.dev"},
            ),
        ],
        {"class": "greeting", "href": "https://boot.dev"},
    )
    node_triple_parent = ParentNode(
        "div",
        [
            ParentNode(
                "div",
                [
                    ParentNode("p", [LeafNode("Bold text", "b")]),
                    LeafNode(
                        "Normal text",
                        "a",
                        {"class": "greeting", "href": "https://boot.dev"},
                    ),
                ],
                {"class": "greeting", "href": "https://boot.dev"},
            )
        ],
    )

    def test_to_html(self):
        expected = """\
<p class="greeting" href="https://boot.dev">
    <b>Bold text</b>
    Normal text
    <i>italic text</i>
    Normal text
</p>"""
        result = self.base_node.to_html()
        self.assertEqual(result, expected)

    def test_to_html_2(self):
        expected = """\
<div class="greeting" href="https://boot.dev">
    <p>
        <b>Bold text</b>
        Normal text
        <i>italic text</i>
        Normal text
    </p>
    <a class="greeting" href="https://boot.dev">Normal text</a>
</div>"""
        result = self.node_with_extra_parent.to_html()
        self.assertEqual(result, expected)
        
    def test_to_html_3(self):
        expected = """\
<div>
    <div class="greeting" href="https://boot.dev">
        <p>
            <b>Bold text</b>
        </p>
        <a class="greeting" href="https://boot.dev">Normal text</a>
    </div>
</div>"""
        result = self.node_triple_parent.to_html()
        self.assertEqual(result, expected)

    def test_values(self):
        result = self.base_node
        self.assertEqual(result.tag, "p")
        self.assertEqual(result.value, None)
        self.assertEqual(
            result.children,
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            result.props, {"class": "greeting", "href": "https://boot.dev"}
        )

    def test_eq(self):
        expected = self.base_node
        result = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(result, expected)

    def test_repr(self):
        expected = "ParentNode(tag='p', value=None, props={'class': 'greeting', 'href': 'https://boot.dev'})"
        result = repr(self.base_node)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = "<p - None>"
        result = str(self.base_node)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
