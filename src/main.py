from textnode import TextNode


def main():
    item = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(repr(item))


if __name__ == "__main__":
    main()
