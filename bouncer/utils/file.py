#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.

from contextlib import contextmanager
from pathlib import Path

from typing_extensions import Generator
from utils.dir import current_dir

from bouncer.constants import allowlist_file, denylist_file

"""
Util file that deals with file operations, such as:
    Open file
    Read file
    Write file
"""


@contextmanager
def open_file(file_path: Path) -> Generator:
    """
    It opens and yields the file object to the caller.
    It needs to be called with a "with" statement.

    Check if file exists:
        True: continue
        False: create file
    """
    if not _is_files_present():
        _create_files()

    f = open(file_path, "r", encoding="utf-8")

    try:
        yield f
    finally:
        f.close()


def read_file(file_path: Path) -> list[str]:
    with open_file(file_path) as f:
        return f.readlines()


def _create_files() -> None:
    """
    Create both allow and deny lists
    """
    open(f"{current_dir}{allowlist_file}", "a", encoding="utf-8").close()
    open(f"{current_dir}{denylist_file}", "a", encoding="utf-8").close()


def write_file(file_path: Path, content: str) -> None:
    with open_file(file_path) as f:
        if f.writable():
            f.write(content)


def _is_files_present() -> bool:
    """
    Check if both allow and deny lists exists
    The filepath is hardcoded, not a great way to do it but meh
    """
    return (
        True
        if (
            Path(f"{current_dir}{allowlist_file}").is_file()
            and Path(f"{current_dir}{denylist_file}").is_file()
        )
        else False
    )
