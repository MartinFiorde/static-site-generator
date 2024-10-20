import shutil
import os


from src.models.text_node import TextNode
from src.services.os_service import *


def main():
    print(f'repr: {repr(TextNode("This is a text node", "bold", "https://www.boot.dev"))}')
    clean_public_dir()
    copy_static_into_public_dir()


if __name__ == "__main__":
    main()
