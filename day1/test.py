import unittest
import rocketequation

class DayOneTest(unittest.TestCase):
    def test_parse(self):
        filename = "input.txt"
        parsed_text = rocketequation.parseInput(filename)
        all_ints = all(isinstance(item, int) for item in parsed_text)
        self.assertTrue(all_ints)

    def test_calculator(self):
        module_list = [14, 15, 100]
        self.assertEqual(rocketequation.fuelCalculator(module_list), 36)

    def test_calculator_2(self):
        module_list = [100756]
        self.assertEqual(rocketequation.fuelCalculator2(module_list), 50346)

if __name__ == '__main__':
    unittest.main()
