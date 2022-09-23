# A file to test the functions within primegenerator.py

import unittest

import primegenerator


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.testPrimeNumList = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
        self.testA_List = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
    
    def test_list_lengths(self):
        resultN, resultA = primegenerator.get_numbers()
        expectedNList = self.testPrimeNumList
        expectedAList = self.testA_List
        self.assertEqual(len(resultN), len(expectedNList), "List size incorrect! Should equal 40")
        self.assertEqual(len(resultA), len(expectedAList), "List size incorrect! Should equal 40")

    def test_prime_numbers(self):
        primeList = primegenerator.test_prime_number()
        self.assertGreaterEqual(len(primeList), 2, "ERROR: Prime List not long enough")

    def test_p_and_q(self):
        resultP, resultQ = primegenerator.get_p_and_q()

        self.assertIsNotNone(resultP)
        self.assertIsNotNone(resultQ)
        
if __name__ == '__main__':
    unittest.main()