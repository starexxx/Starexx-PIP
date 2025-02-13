import argparse
from .core import scan_and_install

def main():
    parser = argparse.ArgumentParser(description="Auto-install missing Python modules.")
    parser.add_argument("--run", action="store_true", help="Run starexx to install dependencies.")
    args = parser.parse_args()

    if args.run:
        scan_and_install()

if __name__ == "__main__":
    main()
