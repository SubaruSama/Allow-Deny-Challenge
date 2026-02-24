#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.

import unittest

from bouncer import core

# 1. Test the instantiation of the AllowList class
# 2. Check if the file list is created at the right directory, lists/allowlist.txt
# 3. Check if the insertion of a URL following the constraints has been successful
# 4. Check if the insertion of a URL that does not follow the constraint results in a error
# 5. Check if the insertion of a URL without any schemes will result in addition of `http://`


# Test suite
class TestAllowList(unittest.TestCase):
    # Test cases
    @unittest.skip("Need to check how to work with mocks and temp files")
    def test_add_url_to_allowlist(self):
        self.assertTrue(
            core.add_to_allowlist("https://example.com"),
            "It should return True, meaning it had no probelms adding such URL",
        )

    @unittest.skip("Need to check how to work with mocks and temp files")
    def test_add_url_to_denylist(self):
        self.assertTrue(
            core.add_to_denylist("https://example.com"),
            "It should return True, meaning it had no problemas adding such URL",
        )

    @unittest.skip("Need to check how to work with mocks and temp files")
    def test_insert_invalid_scheme(self):
        self.assertFalse(
            core.add_to_allowlist("smtp://example.com")
            and core.add_to_denylist("smtp://example.com")
        )

    def test_statistics(self):
        stats = core.statistics()

        self.assertIsInstance(stats, dict)
        for key, value in stats.items():
            self.assertIsInstance(key, str, f"{key} must be a string")
            self.assertIsInstance(value, int, f"{value} must be a int")

    def test_get_content(self):
        self.assertTrue(
            core.get_allowlist() and core.get_denylist(),
            "If the file allowlists does not have any line text, it means its empty",
        )


if __name__ == "__main__":
    unittest.main()
