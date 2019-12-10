import unittest
import gravityassist

class DayTwoTest(unittest.TestCase):
    def test_parse(self):
        filename = "input.txt"
        parsed_text = gravityassist.parseInput(filename)
        all_ints = all(isinstance(item, int) for item in parsed_text)
        self.assertTrue(all_ints)

    def test_gravityprogram(self):
        input1 = [1,9,10,3,2,3,11,0,99,30,40,50]
        input2 = [1,0,0,0,99]
        input3 = [2,4,4,5,99,0]
        input4 = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(gravityassist.gravityProgram(input1),
                         [3500,9,10,70,2,3,11,0,99,30,40,50])
        self.assertEqual(gravityassist.gravityProgram(input2),
                         [2,0,0,0,99])
        self.assertEqual(gravityassist.gravityProgram(input3),
                         [2,4,4,5,99,9801])
        self.assertEqual(gravityassist.gravityProgram(input4),
                         [30,1,1,4,2,5,6,0,99])

    def test_nounverbfinder(self):
        filename = "input.txt"
        puzzle_input = gravityassist.parseInput(filename)
        (noun, verb) = gravityassist.nounVerbFinder(puzzle_input, 4023471)
        self.assertEqual(noun, 12)
        self.assertEqual(verb, 2)

if __name__ == '__main__':
    unittest.main()
