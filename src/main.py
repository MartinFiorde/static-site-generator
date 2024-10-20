import shutil
import os

from src.models.text_node import TextNode

PUBLIC_PATH = "./public"
STATIC_PATH = "./static"


def main():
    item = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(f"str: {str(item)}")
    print(f"repr: {repr(item)}")
    clean_public_dir()
    copy_static_into_public_dir()


def clean_public_dir(path=PUBLIC_PATH):
    if not os.path.exists(path):
        if path == PUBLIC_PATH:
            os.mkdir(path)
        else:
            raise OSError("Referenced directory not found.")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                clean_public_dir(item_path)
                os.rmdir(item_path)
        except Exception as e:
            raise e


def copy_static_into_public_dir(origin=STATIC_PATH, destination=PUBLIC_PATH):
    if not os.path.exists(origin):
        if origin == STATIC_PATH:
            return
        else:
            raise OSError("Referenced directory not found.")
    for item in os.listdir(origin):
        origin_item_path = os.path.join(origin, item)
        destination_item_path = os.path.join(destination, item)
        try:
            if os.path.isfile(origin_item_path) or os.path.islink(origin_item_path):
                shutil.copy(origin_item_path, destination_item_path)
            elif os.path.isdir(origin_item_path):
                os.mkdir(destination_item_path)
                copy_static_into_public_dir(origin_item_path, destination_item_path)
        except Exception as e:
            raise e


if __name__ == "__main__":
    main()
