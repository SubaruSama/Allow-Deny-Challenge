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

import os
from pathlib import Path
from urllib.parse import urlparse

from classes.exceptions import InvalidSchemeInURL, MissingSchemeInURL
from constants import (
    allowed_schemes,
    allowlist_file,
    denylist_file,
)
from utils.dir import current_dir

CURRENT_DIR = current_dir


def add_to_denylist(url: str) -> None:
    pass


def get_denylist() -> list[str]:
    return []


def add_to_allowlist(url: str) -> None:
    pass


def get_allowlist() -> list[str]:
    return []


def statistics() -> dict[str, int]:
    return {"total": 0}


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
    return False if parsed.scheme not in allowed_schemes else True


def _add_default_scheme(url: str) -> str:
    default_scheme = "http://"
    return f"{default_scheme}{url}"
