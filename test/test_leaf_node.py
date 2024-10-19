import unittest

from src.models.leaf_node import LeafNode
from src.models.text_node import TextNode, TextType


class TestLeafNode(unittest.TestCase):
    base_node = LeafNode(
        "Hello, world!", "a", {"class": "greeting", "href": "https://boot.dev"}
    )

    def test_to_html(self):
        expected = '<a class="greeting" href="https://boot.dev">Hello, world!</a>'
        result = self.base_node.to_html()
        self.assertEqual(result, expected)

    def test_text_node_to_html_node(self):
        expected = LeafNode(tag=None, value="Simple text without tag", props={})
        result = LeafNode.text_node_to_html_node(
            TextNode("Simple text without tag", TextType.TEXT)
        )
        self.assertEqual(result, expected)
        expected = LeafNode(tag="b", value="Bold text", props={})
        result = LeafNode.text_node_to_html_node(TextNode("Bold text", TextType.BOLD))
        self.assertEqual(result, expected)
        expected = LeafNode(tag="i", value="Italic text", props={})
        result = LeafNode.text_node_to_html_node(
            TextNode("Italic text", TextType.ITALIC)
        )
        self.assertEqual(result, expected)
        expected = LeafNode(tag="code", value="code example", props={})
        result = LeafNode.text_node_to_html_node(
            TextNode("code example", TextType.CODE)
        )
        self.assertEqual(result, expected)
        expected = LeafNode(
            tag="a", value="link to something", props={"href": "https://boot.dev"}
        )
        result = LeafNode.text_node_to_html_node(
            TextNode("link to something", TextType.LINK, "https://boot.dev")
        )
        self.assertEqual(result, expected)
        expected = LeafNode(
            tag="img",
            value="",
            props={
                "src": "https://www.boot.dev/img/bootdev-logo-full-small.webp",
                "alt": "Boot.dev",
            },
        )
        result = LeafNode.text_node_to_html_node(
            TextNode(
                "Boot.dev",
                TextType.IMAGE,
                "https://www.boot.dev/img/bootdev-logo-full-small.webp",
            )
        )
        self.assertEqual(result, expected)

    def test_values(self):
        result = self.base_node
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "Hello, world!")
        self.assertEqual(result.children, [])
        self.assertEqual(
            result.props, {"class": "greeting", "href": "https://boot.dev"}
        )

    def test_eq(self):
        expected = self.base_node
        result = LeafNode(
            "Hello, world!",
            "a",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(result, expected)

    def test_repr(self):
        expected = "LeafNode(tag='a', value='Hello, world!', props={'class': 'greeting', 'href': 'https://boot.dev'})"
        result = repr(self.base_node)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = "<a - Hello, world!>"
        result = str(self.base_node)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
