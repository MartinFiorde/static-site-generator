import unittest

from src.services.markdown_service import *
from src.services.text_node_service import *


class TestMarkdownService(unittest.TestCase):

    # markdown_to_html_node() tests

    def test_markdown_to_html_node_simple_paragraph(self):
        base = "**text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode(tag="b", value="text", props={}),
                        LeafNode(tag=None, value=" with an ", props={}),
                        LeafNode(tag="i", value="italic", props={}),
                        LeafNode(tag=None, value=" word and a ", props={}),
                        LeafNode(tag="code", value="code block", props={}),
                        LeafNode(tag=None, value=" and an ", props={}),
                        LeafNode(
                            tag="img",
                            value="",
                            props={
                                "src": "https://i.imgur.com/fJRm4Vk.jpeg",
                                "alt": "obi wan image",
                            },
                        ),
                        LeafNode(tag=None, value=" and a ", props={}),
                        LeafNode(
                            tag="a", value="link", props={"href": "https://boot.dev"}
                        ),
                    ],
                    props={},
                )
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_simple_heading(self):
        base = "###### Simple heading"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="h6",
                    children=[LeafNode(tag=None, value="Simple heading", props={})],
                    props={},
                )
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_simple_code_block(self):
        base = "```\ndef simple_block_code(example):\n    return example*2\n\n```"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="pre",
                    children=[
                        LeafNode(
                            tag="code",
                            value="def simple_block_code(example):\n    return example*2\n",
                            props={},
                        )
                    ],
                    props={},
                )
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_simple_quote(self):
        base = "> first **quote**\n> **quote** 2° line"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="blockquote",
                    children=[
                        ParentNode(
                            tag="p",
                            children=[
                                LeafNode(tag=None, value="first ", props={}),
                                LeafNode(tag="b", value="quote", props={}),
                            ],
                            props={},
                        ),
                        ParentNode(
                            tag="p",
                            children=[
                                LeafNode(tag="b", value="quote", props={}),
                                LeafNode(tag=None, value=" 2° line", props={}),
                            ],
                            props={},
                        ),
                    ],
                    props={},
                )
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_simple_u_list(self):
        base = "* first list first item\n* first list 2° line\n- 2° list first item"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="ul",
                    children=[
                        ParentNode(
                            tag="li",
                            children=[
                                LeafNode(
                                    tag=None, value="first list first item", props={}
                                )
                            ],
                            props={},
                        ),
                        ParentNode(
                            tag="li",
                            children=[
                                LeafNode(tag=None, value="first list 2° line", props={})
                            ],
                            props={},
                        ),
                    ],
                    props={},
                ),
                ParentNode(
                    tag="ul",
                    children=[
                        ParentNode(
                            tag="li",
                            children=[
                                LeafNode(tag=None, value="2° list first item", props={})
                            ],
                            props={},
                        )
                    ],
                    props={},
                ),
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_simple_o_list(self):
        base = "1. first item\n123. second item"
        expected = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="ol",
                    children=[
                        ParentNode(
                            tag="li",
                            children=[LeafNode(tag=None, value="first item", props={})],
                            props={},
                        ),
                        ParentNode(
                            tag="li",
                            children=[
                                LeafNode(tag=None, value="second item", props={})
                            ],
                            props={},
                        ),
                    ],
                    props={},
                )
            ],
            props={},
        )
        result = markdown_to_html_node(base)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
