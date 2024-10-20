import unittest

from src.services.os_service import *


class TestOsService(unittest.TestCase):

    # extract_title() tests

    def test_extract_title_with_h1(self):
        expected = "This md has h1 title"
        result = extract_title("#     This md has h1 title")
        self.assertEqual(result, expected)

    def test_extract_title_without_h1(self):
        with self.assertRaises(Exception) as context:
            extract_title("## this md doesnt have h1 title")
        self.assertEqual(
            repr(context.exception),
            "Exception('Markdown document is invalid. H1 header not found.')",
        )


if __name__ == "__main__":
    unittest.main()
