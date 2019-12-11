import unittest
import monitoringstation

class DayTenTest(unittest.TestCase):
    def test_partone_1(self):
        map = monitoringstation.parseInput('input2.txt')
        asteroids, coordinates = monitoringstation.partOne(map)
        self.assertEqual(asteroids, 33)
        self.assertEqual(coordinates, (5,8))

    def test_partone_2(self):
        map = monitoringstation.parseInput('input3.txt')
        asteroids, coordinates = monitoringstation.partOne(map)
        self.assertEqual(asteroids, 35)
        self.assertEqual(coordinates, (1,2))

    def test_partone_3(self):
        map = monitoringstation.parseInput('input4.txt')
        asteroids, coordinates = monitoringstation.partOne(map)
        self.assertEqual(asteroids, 41)
        self.assertEqual(coordinates, (6,3))

    def test_partone_4(self):
        map = monitoringstation.parseInput('input5.txt')
        asteroids, coordinates = monitoringstation.partOne(map)
        self.assertEqual(asteroids, 210)
        self.assertEqual(coordinates, (11,13))

    def test_parttwo_1(self):
        map = monitoringstation.parseInput('input5.txt')
        asteroid = monitoringstation.partTwo(map, 1)
        self.assertEqual(asteroid, (11,12))
        asteroid = monitoringstation.partTwo(map, 200)
        self.assertEqual(asteroid, (8,2))
        asteroid = monitoringstation.partTwo(map, 201)
        self.assertEqual(asteroid, (10,9))
        asteroid = monitoringstation.partTwo(map, 299)
        self.assertEqual(asteroid, (11,1))

if __name__ == '__main__':
    unittest.main()
