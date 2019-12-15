import unittest
import chemicals

class DaysFourteenTest(unittest.TestCase):
    def test_ore_1(self):
        filename = "input2.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partOne(puzzle_input), 31)

    def test_ore_2(self):
        filename = "input3.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partOne(puzzle_input), 165)

    def test_ore_3(self):
        filename = "input4.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partOne(puzzle_input), 13312)

    def test_ore_4(self):
        filename = "input5.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partOne(puzzle_input), 180697)

    def test_ore_5(self):
        filename = "input6.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partOne(puzzle_input), 2210736)

    def test_fuel_1(self):
        filename = "input4.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partTwo(puzzle_input), 82892753)

    def test_fuel_2(self):
        filename = "input5.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partTwo(puzzle_input), 5586022)

    def test_fuel_3(self):
        filename = "input6.txt"
        puzzle_input = chemicals.parseInput(filename)
        self.assertEqual(chemicals.partTwo(puzzle_input), 460664)

if __name__ == '__main__':
    unittest.main()
