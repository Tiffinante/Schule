import unittest
from Eintritt import eintritt


class EintrittTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(eintritt(0), 0)
        self.assertEqual(eintritt(3), 6)

if __name__ == "__main__":
    unittest.main()