# Remember, it's bad for automation to fail silently

from rearrange import rearrange_name
import unittest


# Inheriting TestCase class
class TestRearrange(unittest.TestCase):

    # Any methods we define in our TestRearrange class that start with the prefix test will automatically become tests that can be run by the testing framework
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Volatire"
        expected = "Volatire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
