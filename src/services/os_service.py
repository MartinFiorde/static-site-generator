import shutil
import os
import re

from src.services.markdown_service import markdown_to_html_node

PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
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


def copy_static_into_public_dir(from_path=STATIC_PATH, dest_path=PUBLIC_PATH):
    if not os.path.exists(from_path):
        if from_path == STATIC_PATH:
            return
        else:
            raise OSError("Referenced path not found.")
    for item in os.listdir(from_path):
        origin_item_path = os.path.join(from_path, item)
        destination_item_path = os.path.join(dest_path, item)
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


def generate_page(from_path, dest_path, template_path=TEMPLATE_PATH):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    content_as_md = ""
    with open(from_path, "r", encoding="utf-8") as file:
        content_as_md = "".join(file.readlines())
    title = extract_title(content_as_md)
    content_as_html = markdown_to_html_node(content_as_md).to_html()

    file_content = ""
    with open(template_path, "r", encoding="utf-8") as file:
        file_content = "".join(file.readlines())
    file_content = file_content.replace(" {{ Title }} ", title, 1)
    file_content = file_content.replace("{{ Content }}", content_as_html, 1)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(file_content)


def generate_pages_recursive(file_path=CONTENT_PATH, dest_path=PUBLIC_PATH):
    for item in os.listdir(file_path):
        origin_item_path = os.path.join(file_path, item)
        try:
            if os.path.isfile(origin_item_path):
                file_name, extension = os.path.splitext(item)
                if extension == ".md":
                    generate_page(origin_item_path, f"{dest_path}/{file_name}.html")
            elif os.path.isdir(origin_item_path):
                destination_item_path = os.path.join(dest_path, item)
                generate_pages_recursive(origin_item_path, destination_item_path)
        except Exception as e:
            raise e
