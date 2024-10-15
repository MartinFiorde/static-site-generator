import unittest

from src.models.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    base_node = LeafNode(
        "Hello, world!", "a", {"class": "greeting", "href": "https://boot.dev"}
    )

    def test_to_html(self):
        expected = '<a class="greeting" href="https://boot.dev">Hello, world!</a>'
        result = self.base_node.to_html()
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
        expected = "<Hello, world! - a>"
        result = str(self.base_node)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
