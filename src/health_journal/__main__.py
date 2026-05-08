"""Command-line interface for Health Journal."""

import argparse
import sys
from health_journal import __version__
from health_journal.cli import setup_wellness_parser


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="health_journal",
        description="Health Journal - A tool for tracking health data"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    # Add subcommands
    subparsers = parser.add_subparsers(dest="command")
    setup_wellness_parser(subparsers)

    args = parser.parse_args()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    # Execute command
    if hasattr(args, "func"):
        return args.func(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
