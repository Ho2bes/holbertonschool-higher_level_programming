#!/usr/bin/python3
"""Unit tests for max_integer function"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

        # Test with a list containing a single integer
        self.assertEqual(max_integer([100]), 100)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing duplicate integers
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

        # Test with a list containing mixed types
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, '4'])
