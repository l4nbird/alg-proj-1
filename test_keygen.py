import unittest
import proj1_keygen
import primegenerator

class TestKeyGeneration(unittest.TestCase):
    def setUp(self):
        resultP, resultQ = primegenerator.get_p_and_q()
        self.phi = (resultP - 1) * (resultQ - 1)
    def test_get_public_key(self):
        expected = self.phi
        result = proj1_keygen.getPublicKey.phi
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()