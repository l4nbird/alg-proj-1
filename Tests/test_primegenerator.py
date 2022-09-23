# A file to test the functions within primegenerator.py

import unittest
from primegenerator import *

class testGetNumbers(unittest.TestCase):
    def setUp(self):
        self.TestPrimeNumList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.TestA_List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.x = 1000000
        self.n
        self.a
    
    def test_list_lengths(self):
        result = len(get_numbers.primeNumList)
        expected=  len(testGetNumbers.TestPrimeNumList)
        self.assertEqual(len(expected), len(result))
