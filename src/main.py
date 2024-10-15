from models.text_node import TextNode


def main():
    item = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(f"str: {str(item)}")
    print(f"repr: {repr(item)}")


if __name__ == "__main__":
    main()
