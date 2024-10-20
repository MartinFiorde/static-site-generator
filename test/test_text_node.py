import unittest
import copy

from src.models.text_node import TextNode, TextType
from src.models.leaf_node import LeafNode


class TestTextNode(unittest.TestCase):
    base_node_without_url = TextNode("This is a text node", TextType.BOLD)
    base_text_node = TextNode("base text", TextType.ITALIC, "base url")

    def test_values(self):
        result = self.base_text_node
        self.assertEqual(result.text, "base text")
        self.assertEqual(result.text_type, TextType.ITALIC.value)
        self.assertEqual(result.url, "base url")

    def test_eq(self):
        expected = TextNode("This is a text node", TextType.BOLD)
        result = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_eq_explicit_None_url(self):
        expected = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(self.base_node_without_url, expected)

    def test_repr(self):
        expected = "TextNode(text='This is a text node', text_type='bold', url=None)"
        result = repr(self.base_node_without_url)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = "<This is a text node - bold - None>"
        result = str(self.base_node_without_url)
        self.assertEqual(result, expected)

    def test_text_change(self):
        expected = TextNode("This is the new text", TextType.BOLD)
        result = copy.deepcopy(self.base_node_without_url)
        result.text = "This is the new text"
        self.assertEqual(result, expected)
        self.assertEqual(result.text, expected.text)

    def test_text_change_to_None(self):
        expected = TextNode(None, TextType.BOLD)
        result = copy.deepcopy(self.base_node_without_url)
        result.text = None
        self.assertEqual(result, expected)
        self.assertEqual(result.text, expected.text)

    def test_diferent_text(self):
        result = TextNode("diferent text", TextType.ITALIC, "base url")
        self.assertNotEqual(result, self.base_text_node)
        self.assertEqual(result.text_type, self.base_text_node.text_type)
        self.assertEqual(result.url, self.base_text_node.url)
        self.assertNotEqual(result.text, self.base_text_node.text)

    def test_diferent_text_type(self):
        result = TextNode("base text", TextType.CODE, "base url")
        self.assertNotEqual(result, self.base_text_node)
        self.assertEqual(result.text, self.base_text_node.text)
        self.assertEqual(result.url, self.base_text_node.url)
        self.assertNotEqual(result.text_type, self.base_text_node.text_type)

    def test_diferent_url(self):
        result = TextNode("base text", TextType.ITALIC, "diferent url")
        self.assertNotEqual(result, self.base_text_node)
        self.assertEqual(result.text, self.base_text_node.text)
        self.assertEqual(result.text_type, self.base_text_node.text_type)
        self.assertNotEqual(result.url, self.base_text_node.url)

    def test_text_node_to_html_node_text(self):
        expected = LeafNode(tag=None, value="Simple text without tag", props={})
        result = TextNode(
            "Simple text without tag", TextType.TEXT
        ).text_node_to_html_node()
        self.assertEqual(result, expected)
        
    def test_text_node_to_html_node_bold(self):
        expected = LeafNode(tag="b", value="Bold text", props={})
        result = TextNode("Bold text", TextType.BOLD).text_node_to_html_node()
        self.assertEqual(result, expected)
        
    def test_text_node_to_html_node_italic(self):
        expected = LeafNode(tag="i", value="Italic text", props={})
        result = TextNode("Italic text", TextType.ITALIC).text_node_to_html_node()
        self.assertEqual(result, expected)
        
    def test_text_node_to_html_node_code(self):
        expected = LeafNode(tag="code", value="code example", props={})
        result = TextNode("code example", TextType.CODE).text_node_to_html_node()
        self.assertEqual(result, expected)
        
    def test_text_node_to_html_node_link(self):
        expected = LeafNode(
            tag="a", value="link to something", props={"href": "https://boot.dev"}
        )
        result = TextNode(
            "link to something", TextType.LINK, "https://boot.dev"
        ).text_node_to_html_node()
        self.assertEqual(result, expected)
        
    def test_text_node_to_html_node_image(self):
        expected = LeafNode(
            tag="img",
            value="",
            props={
                "src": "https://www.boot.dev/img/bootdev-logo-full-small.webp",
                "alt": "Boot.dev",
            },
        )
        result = TextNode(
            "Boot.dev",
            TextType.IMAGE,
            "https://www.boot.dev/img/bootdev-logo-full-small.webp",
        ).text_node_to_html_node()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
