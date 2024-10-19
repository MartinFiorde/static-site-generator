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
        
'''
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

    def test_split_nodes_delimiter_bold_double(self):
        base = "**bold**, follow by normal again, follow by **extra bold again**"
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again, follow by ", TextType.TEXT),
            TextNode("extra bold again", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_triple(self):
        base = "**bold**, follow by normal again, follow by **extra bold again** and **bold a third time**"
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again, follow by ", TextType.TEXT),
            TextNode("extra bold again", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold a third time", TextType.BOLD),
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

    def test_split_nodes_delimiter_link_middle(self):
        base = "This is normal text, follow by [an internal link](https://www.markdownguide.org), follow by normal again"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode(
                "an internal link",
                TextType.LINK,
                "https://www.markdownguide.org",
            ),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, None, TextType.LINK)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_link_double(self):
        base = "This is normal text, follow by [an internal link](https://www.markdownguide.org), follow by normal again, follow by [an internal link again](https://www.markdownguide.org)"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode(
                "an internal link",
                TextType.LINK,
                "https://www.markdownguide.org",
            ),
            TextNode(", follow by normal again, follow by ", TextType.TEXT),
            TextNode(
                "an internal link again",
                TextType.LINK,
                "https://www.markdownguide.org",
            ),
        ]
        result = split_nodes_delimiter(base, None, TextType.LINK)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_image_middle(self):
        base = "This is normal text, follow by ![an image with alt text](https://www.markdownguide.org/assets/images/tux.png), follow by normal again"
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode(
                "an image with alt text",
                TextType.IMAGE,
                "https://www.markdownguide.org/assets/images/tux.png",
            ),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, None, TextType.IMAGE)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_with_all_node_types(self):
        base = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image",
                TextType.IMAGE,
                "https://i.imgur.com/fJRm4Vk.jpeg",
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode(
                "link",
                TextType.LINK,
                "https://boot.dev",
            ),
        ]

        result = text_to_textnodes(base)
        self.assertEqual(result, expected)
'''

if __name__ == "__main__":
    unittest.main()
