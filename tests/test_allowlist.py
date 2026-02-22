#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long as the name is changed.
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 0. You just DO WHAT THE FUCK YOU WANT TO.

import unittest

from classes import AllowList

# 1. Test the instantiation of the AllowList class
# 2. Check if the file list is created at the right directory, lists/allowlist.txt
# 3. Check if the insertion of a URL following the constraints has been successful
# 4. Check if the insertion of a URL that does not follow the constraint results in a error
# 5. Check if the insertion of a URL without any schemes will result in addition of `http://`


# Test suite
class TestAllowList(unittest.TestCase):
    # Test fixture
    def setUp(self):
        self.allowlist = AllowList()

    def tearDown(self):
        del self.allowlist

    # Test cases
    def test_add_url(self):
        self.assertTrue(
            self.allowlist.add_url("https://example.com"),
            "It should return True, meaning it had no probelms adding such URL",
        )

    def test_statistics(self):
        self.assertGreater(
            self.allowlist.statistics(),
            0,
            "If the file allowlist.txt is not empty, it should return > 0",
        )


if __name__ == "__main__":
    unittest.main()
