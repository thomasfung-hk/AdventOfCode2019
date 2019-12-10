import unittest
import sensorboost

class DayNineTest(unittest.TestCase):
    def test_intcode_1(self):
        program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        output = sensorboost.runComputerWithoutInputs(program)
        self.assertEqual(output, program)

    def test_intcode_2(self):
        program = [1102,34915192,34915192,7,4,7,99,0]
        output = sensorboost.runComputerWithoutInputs(program)
        digits_of_output = len(str(output))
        self.assertEqual(digits_of_output, 16)

    def test_intcode_3(self):
        program = [104,1125899906842624,99]
        output = sensorboost.runComputerWithoutInputs(program)
        self.assertEqual(output, 1125899906842624)

if __name__ == '__main__':
    unittest.main()
