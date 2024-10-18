import unittest

from src.models.text_node import TextNode, TextType
from src.text_node_service import *


class TestTextNodeService(unittest.TestCase):

    def test_split_nodes_delimiter_bold_all(self):
        base = "**bold**"
        expected = [
            TextNode("bold", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_first(self):
        base = "**bold**, follow by normal again"
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_middle(self):
        base = "This is normal text, follow by **bold**, follow by normal again"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_last(self):
        base = "This is normal text, follow by **bold**"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_italic_middle(self):
        base = "This is normal text, follow by *italic*, follow by normal again"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, "*", TextType.ITALIC)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_code_middle(self):
        base = "This is normal text, follow by `code`, follow by normal again"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, "`", TextType.CODE)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
