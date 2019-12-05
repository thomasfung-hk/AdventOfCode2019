import unittest
import crossedwires

class PartThreeTest(unittest.TestCase):
    def test_parse(self):
        filename = "input.txt"
        (parsed_text_1, parsed_text_2) = crossedwires.parseInput(filename)
        all_str_1 = all(isinstance(item, str) for item in parsed_text_1)
        all_str_2 = all(isinstance(item, str) for item in parsed_text_2)
        self.assertTrue(all_str_1)
        self.assertTrue(all_str_2)

    def test_pathSetGen(self):
        target_path_set = {(1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                           (5, 1), (5, 2), (4, 2), (3, 2)}
        generated_path_set = crossedwires.pathSetGen(['R5', 'U2', 'L2'])
        self.assertTrue(target_path_set==generated_path_set)

    def test_closestIntersection_1(self):
        wire_1 = ['R8','U5','L5','D3']
        wire_2 = ['U7','R6','D4','L4']
        self.assertEqual(crossedwires.closestIntersection(wire_1, wire_2), 6)

    def test_closestIntersection_2(self):
        wire_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        wire_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        self.assertEqual(crossedwires.closestIntersection(wire_1, wire_2), 159)

    def test_closestIntersection_3(self):
        wire_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        wire_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        self.assertEqual(crossedwires.closestIntersection(wire_1, wire_2), 135)

    def test_pathListGen(self):
        target_path_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                           (5, 1), (5, 2), (4, 2), (3, 2)]
        generated_path_list = crossedwires.pathListGen(['R5', 'U2', 'L2'])
        self.assertTrue(target_path_list==generated_path_list)

    def test_smallestDelay_1(self):
        wire_1 = ['R8','U5','L5','D3']
        wire_2 = ['U7','R6','D4','L4']
        self.assertEqual(crossedwires.smallestDelay(wire_1, wire_2), 30)

    def test_smallestDelay_2(self):
        wire_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        wire_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        self.assertEqual(crossedwires.smallestDelay(wire_1, wire_2), 610)

    def test_smallestDelay_3(self):
        wire_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        wire_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        self.assertEqual(crossedwires.smallestDelay(wire_1, wire_2), 410)

if __name__ == '__main__':
    unittest.main()
