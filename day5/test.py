import unittest
import intcode

class PartFiveTest(unittest.TestCase):
    def test_intcode_1(self):
        program = [1002,4,3,4,33]
        puzzle_input, output = intcode.intCodeAdvanced(program)
        self.assertEqual(puzzle_input, [1002,4,3,4,99])

    def test_intcode_2(self):
        program = [3,9,8,9,10,9,4,9,99,-1,8]
        puzzle_input, output = intcode.intCodeAdvanced(program, 8)
        self.assertEqual(output, [1])

    def test_intcode_3(self):
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        puzzle_input, output = intcode.intCodeAdvanced(program, 0)
        self.assertEqual(output, [0])

    def test_intcode_4(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        puzzle_input, output = intcode.intCodeAdvanced(program, 0)
        self.assertEqual(output, [999])

    def test_intcode_5(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        puzzle_input, output = intcode.intCodeAdvanced(program, 8)
        self.assertEqual(output, [1000])

    def test_intcode_6(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        puzzle_input, output = intcode.intCodeAdvanced(program, 9)
        self.assertEqual(output, [1001])

if __name__ == '__main__':
    unittest.main()
