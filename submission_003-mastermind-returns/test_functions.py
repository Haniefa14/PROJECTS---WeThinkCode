import unittest
import mastermind
from unittest.mock import patch
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests

class MyTestCase(unittest.TestCase):
    def test_instructions(self):
        for x in range(100):
            code = len(mastermind.create_code())
            x = mastermind.create_code()
            self.assertEqual(code,4)
            self.assertNotIn(0, x)

if __name__ == "__main__":
    unittest.main()