import shutil
import os
import re

from src.services.markdown_service import markdown_to_html_node

PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
TEMPLATE_PATH = "./template.html"


def clean_public_dir(path=PUBLIC_PATH):
    if not os.path.exists(path):
        if path == PUBLIC_PATH:
            os.mkdir(path)
        else:
            raise OSError("Referenced path not found.")
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
            raise OSError("Referenced path not found.")
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


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        if re.match(r"^#\s", line.strip()):
            pair = line.split(" ", 1)
            return pair[1].strip()
    raise Exception("Markdown document is invalid. H1 header not found.")


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    content_as_md = ""
    with open(from_path, "r", encoding="utf-8") as file:
        content_as_md = "".join(file.readlines())
    title = extract_title(content_as_md)
    content_as_html = markdown_to_html_node(content_as_md).to_html()
    print()
    print(content_as_md)
    print()
    # print(content_as_html)
    print()

    file_content = ""
    with open(template_path, "r", encoding="utf-8") as file:
        file_content = "".join(file.readlines())
    file_content = file_content.replace(" {{ Title }} ", title, 1)
    file_content = file_content.replace("{{ Content }}", content_as_html, 1)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(file_content)
