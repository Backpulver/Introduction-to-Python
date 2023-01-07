import unittest

from telefonnaLubov import (nums_to_text, text_to_nums, nums_to_angle, angles_to_nums, is_phone_tastic)


class TestNumsToText(unittest.TestCase):
    """Test the nums_to_text function."""

    def test_simple_conversion(self):
        self.assertEqual(nums_to_text([2, 2, 2, 2, 2,
                                       3,
                                       4,
                                       5,
                                       -1,
                                       -1,
                                       1,
                                       5,
                                       6, 6, -1, 6,
                                       7, 7, 7, 7, 7, 7,
                                       8,
                                       9, 9, 9, 9, 9, 
                                       0, 0, 0, 0, 2]).upper(), "BDGJJNMQTW A")


class TestTextToNums(unittest.TestCase):
    """Test the text_to_nums function."""

    def test_text_to_num_conversion(self):
        self.assertEqual(text_to_nums(" AadgJMPS t W Z"),
                         [0, 2, -1, 2, 3, 4, 5, 6, 7, -1, 7, 7, 7, 7, 0, 8, 0, 9, 0, 9, 9, 9, 9])
        self.assertEqual(text_to_nums("adgJMPS t W Z "),
                         [2, 3, 4, 5, 6, 7, -1, 7, 7, 7, 7, 0, 8, 0, 9, 0, 9, 9, 9, 9, 0])
        self.assertEqual(text_to_nums("adgJMPS t WZ "),
                         [2, 3, 4, 5, 6, 7, -1, 7, 7, 7, 7, 0, 8, 0, 9, -1, 9, 9, 9, 9, 0])
        self.assertEqual(text_to_nums("LLL"), [5, 5, 5, -1, 5, 5, 5, -1, 5, 5, 5])
        self.assertEqual(text_to_nums(""), [])

class TestNumsToAngles(unittest.TestCase):
    """Test the nums_to_angle function."""

    def test_num_to_angle_conversion(self):
        self.assertEqual(nums_to_angle([1]), 30)
        self.assertEqual(nums_to_angle([1, 9, 3, 2]), 90)
        self.assertEqual(nums_to_angle([6, 6]), 0)


class TestAnglesToNums(unittest.TestCase):
    """Test the angles_to_nums function."""

    def test_angles_to_nums_conversion(self):
        self.assertEqual(angles_to_nums([10, 389, -20, 150, 200, 0]), [1, 5, 7])


class TestIsPhonetastic(unittest.TestCase):
    """Test the is_phone_tastic function."""

    def test_words(self):
        self.assertTrue(is_phone_tastic('a'))
        self.assertFalse(is_phone_tastic("asl pls"))
        self.assertFalse(is_phone_tastic("  asl  pls   "))
        self.assertTrue(is_phone_tastic("LLL"))
        self.assertFalse(is_phone_tastic(""))


if __name__ == '__main__':
    unittest.main()