import unittest

from src.models.text_node import TextNode, TextType
from src.text_node_service import *


class TestTextNodeService(unittest.TestCase):

    # pick_delimiter() tests

    def test_pick_delimiter(self):
        self.assertEqual(pick_delimiter(TextType.BOLD), "**")
        self.assertEqual(pick_delimiter(TextType.ITALIC), "*")
        self.assertEqual(pick_delimiter(TextType.CODE), "`")

        self.assertIsNone(pick_delimiter(TextType.TEXT))
        self.assertIsNone(pick_delimiter(TextType.LINK))
        self.assertIsNone(pick_delimiter(TextType.IMAGE))
        self.assertIsNone(pick_delimiter(None))
        self.assertIsNone(pick_delimiter("invalid data type"))

    # nodify() tests

    def test_nodify_with_string(self):
        base = "this is a normal string"
        expected = [TextNode("this is a normal string", TextType.TEXT)]
        result = nodify(base)
        self.assertEqual(result, expected)

    def test_nodify_with_empty_string(self):
        base = ""
        expected = []
        result = nodify(base)
        self.assertEqual(result, expected)

    def test_nodify_raises_type_error_with_none(self):
        base = None
        expected = "TypeError('Parameter must be a valid string.')"
        with self.assertRaises(Exception) as context:
            nodify(base)
        self.assertEqual(repr(context.exception), expected)

    def test_nodify_raises_type_error_with_invalid_type(self):
        base = 3
        expected = "TypeError('Parameter must be a valid string.')"
        with self.assertRaises(Exception) as context:
            nodify(base)
        self.assertEqual(repr(context.exception), expected)

    # split_nodes_delimiter() tests

    def test_split_nodes_delimiter_raises_Exception_with_bold_invalid(self):
        base = nodify("**bold")
        expected = (
            "Exception('Invalid Markdown syntax, one closing delimiter is missing.')"
        )
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(repr(context.exception), expected)

    def test_split_nodes_delimiter_bold_all(self):
        base = nodify("**bold**")
        expected = [
            TextNode("bold", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_first(self):
        base = nodify("**bold**, follow by normal again")
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_middle(self):
        base = nodify("This is normal text, follow by **bold**, follow by normal again")
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_last(self):
        base = nodify("This is normal text, follow by **bold**")
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_double(self):
        base = nodify(
            "**bold**, follow by normal again, follow by **extra bold again**"
        )
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again, follow by ", TextType.TEXT),
            TextNode("extra bold again", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_bold_triple(self):
        base = nodify(
            "**bold**, follow by normal again, follow by **extra bold again** and **bold a third time**"
        )
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(", follow by normal again, follow by ", TextType.TEXT),
            TextNode("extra bold again", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold a third time", TextType.BOLD),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_italic_middle(self):
        base = nodify("This is normal text, follow by *italic*, follow by normal again")
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, TextType.ITALIC)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_code_middle(self):
        base = nodify("This is normal text, follow by `code`, follow by normal again")
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, TextType.CODE)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_normal_string(self):
        base = nodify("This is a string without markdown content")
        expected = [
            TextNode("This is a string without markdown content", TextType.TEXT),
        ]
        result = split_nodes_delimiter(base, TextType.BOLD)
        result = split_nodes_delimiter(result, TextType.ITALIC)
        result = split_nodes_delimiter(result, TextType.CODE)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_empty_string(self):
        base = nodify("")
        expected = []
        result = split_nodes_delimiter(base, TextType.BOLD)
        result = split_nodes_delimiter(result, TextType.ITALIC)
        result = split_nodes_delimiter(result, TextType.CODE)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_with_basic_node_types(self):
        base = nodify(
            "This is **text** with an *italic* word and a `code block` and repeat. This is **text** with an *italic* word and a `code block` again."
        )
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and repeat. This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" again.", TextType.TEXT),
        ]

        result = split_nodes_delimiter(base, TextType.BOLD)
        result = split_nodes_delimiter(result, TextType.ITALIC)
        result = split_nodes_delimiter(result, TextType.CODE)
        self.assertEqual(result, expected)

    # pattern_selector() tests

    def test_pattern_selector_with_image(self):
        self.assertEqual(pattern_selector(TextType.IMAGE), r"(!\[.*?\]\(.*?\))")

    def test_pattern_selector_with_link(self):
        self.assertEqual(pattern_selector(TextType.LINK), r"(\[.*?\]\(.*?\))")

    def test_pattern_selector_with_other(self):
        with self.assertRaises(Exception) as context:
            pattern_selector(TextType.TEXT)
        self.assertEqual(repr(context.exception), "TypeError('TextType invalid.')")

    # split_nodes_with_url() tests

    def test_split_nodes_with_url_link_middle(self):
        base = nodify(
            "This is normal text, follow by [an internal link](https://www.markdownguide.org), follow by normal again"
        )
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode(
                "an internal link",
                TextType.LINK,
                "https://www.markdownguide.org",
            ),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_with_url(base, TextType.LINK)
        self.assertEqual(result, expected)

    def test_split_nodes_with_url_link_double(self):
        base = nodify(
            "This is normal text, follow by [an internal link](https://www.markdownguide.org), follow by normal again, follow by [an internal link again](https://www.markdownguide.org)"
        )
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
        result = split_nodes_with_url(base, TextType.LINK)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_image_middle(self):
        base = nodify(
            "This is normal text, follow by ![an image with alt text](https://www.markdownguide.org/assets/images/tux.png), follow by normal again"
        )
        expected = [
            TextNode("This is normal text, follow by ", TextType.TEXT),
            TextNode(
                "an image with alt text",
                TextType.IMAGE,
                "https://www.markdownguide.org/assets/images/tux.png",
            ),
            TextNode(", follow by normal again", TextType.TEXT),
        ]
        result = split_nodes_with_url(base, TextType.IMAGE)
        self.assertEqual(result, expected)

    # text_to_textnodes() tests

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

    def test_text_to_textnodes_with_all_node_types_2(self):
        base = "This is a [link](https://boot.dev) with an *italic word* and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a `code block` and a **bold text**."
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode(
                "link",
                TextType.LINK,
                "https://boot.dev",
            ),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic word", TextType.ITALIC),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image",
                TextType.IMAGE,
                "https://i.imgur.com/fJRm4Vk.jpeg",
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]

        result = text_to_textnodes(base)
        self.assertEqual(result, expected)

    # markdown_to_blocks() tests

    def test_markdown_to_blocks(self):
        base = """\
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_code_block(self):
        base = """\
```
{
  "firstName": "John",
  "lastName": "Smith",
         
  "age": 25
}
```



"""
        expected = [
            """\
```
{
  "firstName": "John",
  "lastName": "Smith",
         
  "age": 25
}
```""",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_empty_code_block(self):
        base = """\
```

"""
        expected = ["```\n\n\n```"]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_code_block_not_closed(self):
        base = """\
```
```"""
        expected = ["```\n```"]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_o_list(self):
        base = """\
1. firstName: John,
2.        "lastName": "Smith's",
23423. "age": 25

1.invalid list, lack white space after '1.'"""
        expected = [
            '1. firstName: John,\n2.        "lastName": "Smith\'s",\n23423. "age": 25',
            "1.invalid list, lack white space after '1.'",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_u_list_combined(self):
        base = """\
* first
* second
- first new list
- second new list

- third new list
* single item on last list"""
        expected = [
            "* first\n* second",
            "- first new list\n- second new list\n- third new list",
            "* single item on last list",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_with_quote(self):
        base = """\
> first
> second
> third"""
        expected = [
            "> first\n> second\n> third",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_only_whitespaces(self):
        base = """\
                   

"""
        expected = []
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_headers(self):
        base = """\
# h1
## h2
### h3
#### h4
##### h5
###### h6
####### normal paragraph for invalid head of 7 '#'

"""
        expected = [
            "# h1",
            "## h2",
            "### h3",
            "#### h4",
            "##### h5",
            "###### h6",
            "####### normal paragraph for invalid head of 7 '#'",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_paragraph(self):
        base = """\
this is a normal paragraph
this is another paragraph
this is the last paragraph

"""
        expected = [
            "this is a normal paragraph",
            "this is another paragraph",
            "this is the last paragraph",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_paragraph_with_trails(self):
        base = """\
              this is a normal paragraph with lots of whitesapce at start and end              """
        expected = [
            "this is a normal paragraph with lots of whitesapce at start and end",
        ]
        result = markdown_to_blocks(base)
        self.assertEqual(result, expected)

        # block_to_block_type() tests

    def test_block_to_block_type(self):
        base = [
            "###### this is a heading",
            "####### is a normal paragraph for invalid heading",
            "> this is a quote",
            "* list item\n* another item",
            "1. first\n3. second\n4456. third\n",
            "```\nthis is a code block\n```",
        ]

        result = []
        for block in base:
            result.append(block_to_block_type(block))

        self.assertEqual(result[0], BlockType.HEADING)
        self.assertEqual(result[1], BlockType.PARAGRAPH)
        self.assertEqual(result[2], BlockType.QUOTE)
        self.assertEqual(result[3], BlockType.U_LIST)
        self.assertEqual(result[4], BlockType.O_LIST)
        self.assertEqual(result[5], BlockType.BLOCK_CODE)


if __name__ == "__main__":
    unittest.main()
