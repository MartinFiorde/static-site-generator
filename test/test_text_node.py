import unittest
import copy

from src.models.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    base_node_without_url = TextNode("This is a text node", TextType.BOLD)
    base_text_node = TextNode("base text", TextType.ITALIC, "base url")

    def test_values(self):
        result = self.base_text_node
        self.assertEqual(result.text, "base text")
        self.assertEqual(result.text_type, TextType.ITALIC)
        self.assertEqual(result.url, "base url")

    def test_eq(self):
        expected = TextNode("This is a text node", TextType.BOLD)
        result = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_eq_explicit_None_url(self):
        expected = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(self.base_node_without_url, expected)

    def test_repr(self):
        expected = "TextNode(text='This is a text node', text_type=<TextType.BOLD: 'bold'>, url=None)"
        result = repr(self.base_node_without_url)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = "<This is a text node - TextType.BOLD - None>"
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


if __name__ == "__main__":
    unittest.main()
