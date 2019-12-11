from math import sqrt, atan2, pi

def parseInput(input):
    map = []
    with open(input) as f:
        for line in f:
            map.append(line.strip())
    return map

def asteroidLocator(map):
    height = len(map)
    width = len(map[0])
    asteroids = []
    for y in range(height):
        for x in range(width):
            if map[y][x] == '#':
                asteroids.append((x, y))
    return asteroids


def partOne(puzzle_input):
    asteroids = asteroidLocator(puzzle_input)
    most_asteroids = 0
    coordinates = None
    for asteroid in asteroids:
        x = asteroid[0]
        y = asteroid[1]
        angles = set()
        for asteroid_2 in asteroids:
            if asteroid != asteroid_2:
                x_2, y_2 = asteroid_2
                x_vec = x_2 - x
                y_vec = y - y_2
                angle = atan2(y_vec, x_vec)
                angles.add(angle)
        if len(angles) > most_asteroids:
            coordinates = asteroid
            most_asteroids = len(angles)
    return most_asteroids, coordinates

def partTwo(puzzle_input, num):
    asteroids = asteroidLocator(puzzle_input)
    most_asteroids, coordinates = partOne(puzzle_input)
    asteroids.remove(coordinates)
    asteroidAngles = {}
    x = coordinates[0]
    y = coordinates[1]
    def euclidean(asteroid):
        x_2, y_2 = asteroid
        return sqrt((x - x_2)**2 + (y - y_2)**2)
    asteroids.sort(key=euclidean)
    for asteroid in asteroids:
            x_2, y_2 = asteroid
            x_vec = x_2 - x
            y_vec = y - y_2
            angle = angleModifier(x_vec, y_vec)
            if angle in asteroidAngles:
                asteroidAngles[angle].append(asteroid)
            else:
                asteroidAngles[angle] = [asteroid]
    angles = sorted(asteroidAngles.keys())
    asteroids_destroyed = 0
    i = 0
    while len(angles) > 0:
        angle = angles[i]
        asteroid = asteroidAngles[angle].pop(0)
        asteroids_destroyed += 1
        if asteroids_destroyed == num:
            return asteroid
        if len(asteroidAngles[angle]) == 0:
            angles.remove(angle)
            i = (i)%(len(angles))
        else:
            i = (i + 1)%(len(angles))


def angleModifier(x_vec, y_vec):
    angle = atan2(y_vec, x_vec)
    return ((-1 * angle) + (pi / 2))%(2 * pi)


def main():
    puzzle_input = parseInput('input.txt')
    most_asteroids, coordinates = partOne(puzzle_input)
    print(f"Best is {coordinates} with {most_asteroids} other asteroids detected")
    asteroid = partTwo(puzzle_input, 200)
    print(f"The 200th asteroid is {asteroid}. The output is {asteroid[0]*100+asteroid[1]}.")

if __name__ == '__main__':
    main()
