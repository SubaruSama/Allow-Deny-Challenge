def get_allowed_schemes() -> tuple[str, str, str]:
    return ("http", "https", "ftp")


files: dict[str, str] = {
    "allowlist": "\\bouncer\\data\\allowlist.txt",
    "denylist": "\\bouncer\\data\\denylist.txt",
}

# For future use, use those options to check and create lists and not hardcoding
# allowed_kind = ["allowlist", "denylist"]
