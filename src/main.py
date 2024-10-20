from src.services.os_service import *


def main():
    clean_public_dir()
    copy_static_into_public_dir()
    generate_pages_recursive()


if __name__ == "__main__":
    main()
