import unittest
 
from telefonnaLubov import (nums_to_text, text_to_nums, nums_to_angle,
                      angles_to_nums, is_phone_tastic)
 
 
class TestNumsToText(unittest.TestCase):
    """Test the nums_to_text function."""
 
    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_text([2]).lower(), 'a')
        self.assertEqual(nums_to_text([7, 9, 9, 9, 8, 4, 4, 6, 6, 6, -1, 6, 6]).lower(), 'python')
        self.assertEqual(nums_to_text([2, 0, -1, 0, 2]).lower(), 'a  a')
        self.assertEqual(nums_to_text([2, 0, 0, 2]).lower(), 'a a')
        self.assertEqual(nums_to_text([2, 0, 2]).lower(), 'a a')
        self.assertEqual(nums_to_text([2, 3]).lower(), 'ad')
        self.assertEqual(nums_to_text([0, -1, 0, 2, 0, 2, 3]).lower(), '  a ad')
        self.assertEqual(nums_to_text([2, 2, 2, 2, 2, 2]).lower(), 'c')
        self.assertEqual(nums_to_text([1]), '')
        self.assertEqual(nums_to_text([2, 2, 1, 2, 2]), 'bb')
        self.assertEqual(nums_to_text([2, 2, -1, 2, 2]), 'bb')
        self.assertEqual(nums_to_text([2, 2, 1, 2]), 'ba')
        self.assertEqual(nums_to_text([4, 4, 3, 3, 5, 5, 5, -1, 5, 5, 5, 6, 6, 6, 6, 6, 6]), 'hello')
 
 
class TestTextToNums(unittest.TestCase):
    """Test the text_to_nums function."""
 
    def test_simple_conversion(self):
        """Sanity test for a single letter."""
        self.assertEqual(text_to_nums('a'), [2])
        self.assertEqual(text_to_nums(''), [])
        self.assertEqual(text_to_nums('aaa'), [2, -1, 2, -1, 2])
        self.assertEqual(text_to_nums('a a a'), [2, 0, 2, 0, 2])
        self.assertEqual(text_to_nums('PYTHON'), [7, 9, 9, 9, 8, 4, 4, 6, 6, 6, -1, 6, 6])
        self.assertEqual(text_to_nums('asl pls'), [2, 7, 7, 7, 7, 5, 5, 5, 0, 7, 5, 5, 5, 7, 7, 7, 7])
 
 
class TestNumsToAngles(unittest.TestCase):
    """Test the nums_to_angle function."""
 
    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_angle([1]), 30)
        self.assertEqual(nums_to_angle([1, 5, 9]), 90)
        self.assertEqual(nums_to_angle([9, 2]), 330)
        
 
 
class TestAnglesToNums(unittest.TestCase):
    """Test the angles_to_nums function."""
 
    def test_simple_conversion(self):
        """Sanity test for a single angle."""
        self.assertEqual(angles_to_nums([30]), [1])
        self.assertEqual(angles_to_nums([16, 14, 90, -120]), [1, 3, 8])
        self.assertEqual(angles_to_nums([0, 400, -20, 15]), [1])
        self.assertEqual(angles_to_nums([390, 15, 16, 75]), [1, 1, 2])
        self.assertEqual(angles_to_nums([345]), [])
        self.assertEqual(angles_to_nums([346]), [])
 
 
class TestIsPhonetastic(unittest.TestCase):
    """Test the is_phone_tastic function."""
 
    def test_simple_word(self):
        """Sanity test for a single letter word."""
        self.assertTrue(is_phone_tastic('a'))
        self.assertTrue(is_phone_tastic('GOD'))
        self.assertTrue(is_phone_tastic('LLL'))
        self.assertTrue(is_phone_tastic('sl pls'))
        self.assertFalse(is_phone_tastic(''))
 
 
if __name__ == '__main__':
    unittest.main()