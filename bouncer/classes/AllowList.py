# import os
# from pathlib import Path
# from urllib.parse import urlparse

# from bouncer.classes.exceptions import InvalidSchemeInURL, MissingSchemeInURL

# # from bouncer.constants.allowed_schemes import allowed_schemes

# ALLOWLIST_FILE = "\\bouncer\\data\\allowlist.txt"
# CURRENT_DIR = os.getcwd()


# class AllowList:
#     def __init__(self):
#         pass

#     def __del__(self):
#         pass

#     def _create_file(self) -> None:
#         open(f"{CURRENT_DIR}{ALLOWLIST_FILE}", "a").close()

#     def _is_file_present(self) -> bool:
#         """
#         Method that checks if the file allowlist.txt exists.
#         If true, does nothing
#         If false, create
#         """

#         return True if Path(f"{CURRENT_DIR}{ALLOWLIST_FILE}").is_file() else False

#     def add_url(self, url) -> None:
#         if self._is_file_present():
#             self._create_file()
#         allowlist_file = open(f"{CURRENT_DIR}{ALLOWLIST_FILE}", "a")

#         try:
#             # Primeira validação: checar se existe http://
#             if not self._is_scheme_present(url):
#                 raise MissingSchemeInURL(url)
#             # Segunda validação: checar se o scheme esta dentro das schemes permitidas
#             if not self._is_valid_scheme(url):
#                 raise InvalidSchemeInURL(url)
#             allowlist_file.write(f"{url}\n")
#         except MissingSchemeInURL as e:
#             print(f"Missing any scheme: {e}")
#             print("Adding the default scheme http://")
#             url = self._add_default_scheme(url)
#             allowlist_file.write(f"{url}\n")
#         except InvalidSchemeInURL as e:
#             print(f"Invalid scheme: {e}")
#             exit()
#         finally:
#             allowlist_file.close()

#     def _is_scheme_present(self, url: str) -> bool:
#         """
#         Method that will check if the given URL has any scheme present
#         """
#         parsed = urlparse(url)
#         return True if parsed.scheme != "" else False

#     def _is_valid_scheme(self, url: str) -> bool:
#         """
#         Method that will check if the given URL has the schemes http://, https:// or ftp://
#         """
#         parsed = urlparse(url)
#         return False if parsed.scheme not in allowed_schemes else True

#     def _add_default_scheme(self, url) -> str:
#         default_scheme = "http://"
#         return f"{default_scheme}{url}"

#     def statistics(self) -> int:
#         """
#         Method that will count how much URLs exists in allowlist.txt
#         """
#         return len(self.get_content())

#     def get_content(self) -> list[str]:
#         with open(f"{CURRENT_DIR}{ALLOWLIST_FILE}", "r") as f:
#             contents = f.readlines()

#         return contents
