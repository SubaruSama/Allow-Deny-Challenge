class MissingSchemeInURL(Exception):
    def __init__(
        self, url, message="The given URL does not contain the necessaries schemes"
    ):
        self.url = url
        self.message = f"{message} -> {url}"
        super().__init__(self.message)


class InvalidSchemeInURL(Exception):
    def __init__(self, url, message="The given URL contains an illegal scheme"):
        self.url = url
        self.message = f"{message} -> {url}"
        super().__init__(self.message)
