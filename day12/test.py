import unittest
import jupiter

class DayTwelveTest(unittest.TestCase):
    def test_repeat_state_1(self):
        puzzle_input = ['<x=-8, y=-10, z=0>',
                        '<x=5, y=5, z=10>',
                        '<x=2, y=-7, z=3>',
                        '<x=9, y=-8, z=-3>']
        jupiter_1 = jupiter.Jupiter(puzzle_input)
        self.assertEqual(jupiter_1.find_repeat(), 4686774924)

    def test_repeat_state_2(self):
        puzzle_input = ['<x=-1, y=0, z=2>',
                        '<x=2, y=-10, z=-7>',
                        '<x=4, y=-8, z=8>',
                        '<x=3, y=5, z=-1>']
        jupiter_1 = jupiter.Jupiter(puzzle_input)
        self.assertEqual(jupiter_1.find_repeat(), 2772)

if __name__ == '__main__':
    unittest.main()
