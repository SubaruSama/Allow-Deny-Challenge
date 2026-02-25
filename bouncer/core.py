#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.

"""
It handles the core logic:
    Check if the URL can be inserted at Allow/Deny list
    Check if the scheme is valid
    If the URL is missing a scheme, add a default http://
    Statistics
        Simple
        Summarized by domain
        Count the schemes
"""

from pathlib import Path
from urllib.parse import urlparse

from bouncer.classes.exceptions import (
    InvalidDomainInURL,
    InvalidSchemeInURL,
    MissingSchemeInURL,
)
from bouncer.constants import files, get_allowed_schemes
from bouncer.utils.dir import get_current_dir
from bouncer.utils.file import open_file, read_file, write_file

CURRENT_DIR = get_current_dir()


def add_to_denylist(url: str) -> None:
    pass


def get_denylist() -> list[str]:
    return []


def add_to_allowlist(url: str) -> None:
    allowlist_path: Path = Path(f"{get_current_dir()}\\{Path(files['allowlist'])}")

    try:
        # Check if its valid domain (somethin.xyz), not in the sense of valid in Internet or LAN, only
        # the structure

        # Check if http:// exists
        if not _is_scheme_present(url):
            raise MissingSchemeInURL(url)
        # Check if scheme follows the constraints in scheme (http://, https:// or ftp://)
        if not _is_valid_scheme(url):
            raise InvalidSchemeInURL(url)

        write_file(allowlist_path, url)

    except MissingSchemeInURL as e:
        # add the default scheme here
        print(f"Missing any scheme: {e}")
        print("Adding the default scheme http://")

        url = _add_default_scheme(url)
        write_file(allowlist_path, url)

    except InvalidSchemeInURL as e:
        print(f"Invalid scheme: {e}")
        exit()

    except InvalidDomainInURL as e:
        print(f"Invalid domain: {e}")
        exit()


def get_allowlist() -> list[str]:
    allowlist_path: Path = Path(f"{CURRENT_DIR}{files['allowlist']}")
    results: list[str] = read_file(allowlist_path)

    return results


def statistics() -> dict[str, int]:
    return {}


def statistics_summarized() -> dict[list[str], int]:
    url: list[str] = [""]
    count: int = 0
    result_dict: dict[list[str], int] = {}

    return result_dict


def statistics_scheme() -> dict[list[str], int]:
    url: list[str] = [""]
    count: int = 0
    result_dict: dict[list[str], int] = {}

    return result_dict


def _is_scheme_present(url: str) -> bool:
    parsed = urlparse(url)
    return True if parsed.scheme != "" else False


def _is_valid_scheme(url: str) -> bool:
    parsed = urlparse(url)
    return False if parsed.scheme not in get_allowed_schemes() else True


def _is_valid_domain(url: str) -> bool:
    parsed = urlparse(url)
    return False if parsed.netloc == "" else True


def _add_default_scheme(url: str) -> str:
    default_scheme = "http://"
    return f"{default_scheme}{url}"
