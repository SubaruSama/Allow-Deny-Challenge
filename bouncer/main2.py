#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.

"""
This file a CLI interface, it doesnt holds any logic or configuration.
"""

import sys
from argparse import ArgumentParser, Namespace

import core


def setup_arguments() -> Namespace:
    """
    Function that setup the arguments parser and configures the exclusive commands
    """
    parser = ArgumentParser(
        description="bouncer, your friend to add URLs to your Allow or Deny list"
    )

    # Those functions cant be called at the same time
    exclusive_operations = parser.add_mutually_exclusive_group(required=True)
    exclusive_operations.add_argument(
        "--add-denylist", type=str, help="Add the URL to Denylist"
    )
    exclusive_operations.add_argument(
        "--get-denylist", action="store_true", help="Return the contents of Denylist"
    )
    exclusive_operations.add_argument(
        "--add-allowlist", type=str, help="Add the URL to Allowlist"
    )
    exclusive_operations.add_argument(
        "--get-allowlist", action="store_true", help="Return the contents of Allowlist"
    )

    # For a nice view in CLI
    statistics_operations = parser.add_argument_group("Statistics")
    statistics_operations.add_argument(
        "--statistics",
        action="store_true",
        help="Return the count of URLs in each list",
    )
    statistics_operations.add_argument(
        "--statistics-summarized",
        action="store_true",
        help="Return the count of URLs in each list by domain (TO BE IMPLEMENTED)",
    )
    statistics_operations.add_argument(
        "--statistics-scheme",
        action="store_true",
        help="Return the count of schemes in each list (TO BE IMPLEMENTED)",
    )

    args = parser.parse_args(args=None if sys.argv[1:] else None)

    return args


def main() -> None:
    args = setup_arguments()

    match args:
        case args if args.add_denylist:
            core.add_to_denylist(args.add_denylist)
        case args if args.get_denylist:
            core.get_denylist()
        case args if args.add_allowlist:
            core.add_to_allowlist(args.add_allowlist)
        case args if args.get_allowlist:
            core.get_allowlist()
        case args if args.statistics:
            core.statistics()
        case args if args.statistics_summarized:
            core.statistics_summarized()
        case args if args.statistics_scheme:
            core.statistics_scheme()


if __name__ == "__main__":
    main()
