import unittest
from sorting.bubble_sort import bubble_sort
from test_case_generator import *


class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        ints = integer_array_generator(100)
        self.assertEqual(sorted(ints), bubble_sort(ints))

        floats = float_array_generator(100)
        self.assertEqual(sorted(floats), bubble_sort(floats))

        nums = number_array_generator(100)
        self.assertEqual(sorted(nums), bubble_sort(nums))

        chars = char_array_generator(100)
        self.assertEqual(sorted(chars), bubble_sort(chars))

        strings = string_array_generator(100)
        self.assertEqual(sorted(strings), bubble_sort(strings))


if __name__ == "__main__":
    unittest.main()
