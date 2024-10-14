import unittest

from models.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    base_HTML_node_without_childs = HTMLNode(
        "div",
        "Hello, world!",
        None,
        {"class": "greeting", "href": "https://boot.dev"},
    )


    def test_props_to_html(self):
        expected = ' class="greeting" href="https://boot.dev"'
        result = self.base_HTML_node_without_childs.props_to_html()
        self.assertEqual(result, expected)

    def test_values_with_childs_empty(self):
        result = self.base_HTML_node_without_childs
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.value, "Hello, world!")
        self.assertEqual(result.children, [])
        self.assertEqual(
            result.props, {"class": "greeting", "href": "https://boot.dev"}
        )


    def test_eq(self):
        expected = self.base_HTML_node_without_childs
        result = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(result, expected)

    def test_repr(self):
        expected = "HTMLNode(tag='div', value='Hello, world!', children=[], props={'class': 'greeting', 'href': 'https://boot.dev'})"
        result = repr(self.base_HTML_node_without_childs)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = '<div class="greeting" href="https://boot.dev">Hello, world!</div>'
        result = str(self.base_HTML_node_without_childs)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
