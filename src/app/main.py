"""
Command-line interface for the application.
"""

import argparse
import sys


def cli():
    """Entry point for the application."""
    parser = argparse.ArgumentParser(description="Application CLI")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information and exit",
    )

    args = parser.parse_args()

    if args.version:
        from . import __version__
        print(f"App v{__version__}")
        return 0

    # Add your CLI logic here
    print("Welcome to the application!")
    return 0


if __name__ == "__main__":
    sys.exit(cli()) 