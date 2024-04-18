#
# Alex Cesar Rosa
# 4/21/2024
# ITS Python Certification Review - Problem 1 (Unittest module)
#

import unittest
import display_utils


class TestDisplayUtils(unittest.TestCase):
    def test_get_user_greeting(self):
        greeting = display_utils.get_user_greeting("Bob")
        self.assertEquals(greeting, "Hello Bob!")

    def test_sum_is_greater(self):
        self.assertTrue(display_utils.sum_is_greater(5, 8, 12))


if __name__ == '__main__':
    unittest.main()
