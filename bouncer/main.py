#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.
import argparse
import sys


def arguments():
    parser = argparse.ArgumentParser(
        description="bouncer, interface to add a URL in AllowList or DenyList"
    )
    parser.add_argument("--add-denylist", type=str, help="Add the URL to DenyList")
    parser.add_argument("--add-allowlist", type=str, help="Add the URL to AllowList")
    parser.add_argument(
        "--statistics",
        action="store_true",
        help="Return the count of URLs in each list",
    )
    parser.add_argument(
        "--statistics-summarized",
        action="store_true",
        help="Return the count of URLs in each list by domain (TO BE IMPLEMENTED)",
    )

    return parser.parse_args(args=None if sys.argv[1:] else ["--helpo"])


def main():
    args = arguments()


if __name__ == "__main__":
    main()
