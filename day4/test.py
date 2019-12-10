import unittest
import securecontainer

class DayFourTest(unittest.TestCase):
    def test_neverdecrease(self):
        self.assertTrue(securecontainer.increasingNumber('111111'))
        self.assertFalse(securecontainer.increasingNumber('223450'))

    def test_partone_num(self):
        self.assertTrue(securecontainer.repeatingConsecutiveDigit('223450'))
        self.assertFalse(securecontainer.repeatingConsecutiveDigit('123789'))

    def test_pasttwo_num(self):
        self.assertFalse(securecontainer.repeatingConsecutiveDigit_2('123444'))
        self.assertTrue(securecontainer.repeatingConsecutiveDigit_2('111122'))

if __name__ == '__main__':
    unittest.main()
