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

from bouncer.classes import AllowList, DenyList


def main():
    parser = argparse.ArgumentParser(
        description="bouncer, interface to add a URL in AllowList or DenyList"
    )
    exclusive_operations = parser.add_mutually_exclusive_group(required=True)

    exclusive_operations.add_argument(
        "--add-denylist", type=str, help="Add the URL to DenyList"
    )
    exclusive_operations.add_argument(
        "--get-denylist", action="store_true", help="Return the contents of DenyList"
    )
    exclusive_operations.add_argument(
        "--add-allowlist", type=str, help="Add the URL to AllowList"
    )
    exclusive_operations.add_argument(
        "--get-allowlist", action="store_true", help="Return the contents of AllowList"
    )
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

    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    if args.add_denylist:
        print("[*] Instantiating DenyList")
        denyList = DenyList()
        print(args.add_denylist)
        denyList.__repr__()
    elif args.add_allowlist:
        print("[*] Instantiating AllowList")
        allowList = AllowList()
        print(f"Given URL: {args.add_allowlist}")
        allowList.add_url(args.add_allowlist)

    if args.get_allowlist:
        pass


if __name__ == "__main__":
    main()
