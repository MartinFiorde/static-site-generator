import sys
from src.services.os_service import *


def main():
    base_path = sys.argv[1]
    dest_path = sys.argv[2]

    clean_public_dir(dest_path=dest_path)
    copy_static_into_public_dir(dest_path=dest_path)
    generate_pages_recursive(base_path, dest_path=dest_path)


if __name__ == "__main__":
    main()
