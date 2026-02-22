# from constants import allowed_schemes

ALLOWLIST_FILE = "data/allowlist.txt"


class AllowList:
    def __init__(self):
        print("[*] Resource being created via __init__")

    def __del__(self):
        print("[*] Resource being destroyed via __del__")

    def _create_list(self) -> None:
        file_allowlist = open(ALLOWLIST_FILE)

        if file_allowlist.readable():
            print(f"File {ALLOWLIST_FILE} created")
            file_allowlist.close()

    def _check_list_presence(self) -> bool:
        """
        Method that checks if the file allowlist.txt exists.
        If true, does nothing
        If false, create
        """
        return False

    def add_url(self, url) -> bool:
        return False

    def _check_presence_scheme_in_url(self, url) -> bool:
        """
        Method that will check if the given URL has the schemes http://, https:// or ftp://
        """
        return False

    def _add_default_scheme(self, url) -> str:
        default_scheme = "http://"
        return f"{default_scheme}{url}"

    def statistics(self) -> int:
        """
        Method that will count how much URLs exists in allowlist.txt
        """
        return 0
