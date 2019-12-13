import itertools
import math
import copy

def parseInput(input):
    puzzle_input = []
    with open(input) as f:
        for line in f:
            puzzle_input.append(line.strip())
    return puzzle_input

class Jupiter:
    def __init__(self, puzzle_input):
        self.system = self._make_moons(puzzle_input)
        self.initial = copy.deepcopy(self.system)

    def _make_moons(self, puzzle_input):
        system = []
        for position in puzzle_input:
            moon = Moon(position)
            system.append(moon)
        return system

    def step(self, steps):
        current_step = 0
        moon_pairs = list(itertools.combinations(self.system, 2))
        while current_step < steps:
            for pair in moon_pairs:
                self.apply_gravity(pair)
            for moon in self.system:
                moon.apply_velocity()
            #print(self.total_energy)
            current_step += 1

    def apply_gravity(self, pair):
        moon1, moon2 = pair
        for dimension in Moon.DIMENSIONS:
            if moon1.position[dimension] == moon2.position[dimension]:
                continue
            if moon1.position[dimension] < moon2.position[dimension]:
                increase = moon1
                decrease = moon2
            else:
                increase = moon2
                decrease = moon1
            increase.velocity[dimension] += 1
            decrease.velocity[dimension] -= 1

    @property
    def total_energy(self):
        energy = 0
        for moon in self.system:
            pot = 0
            kin = 0
            for dimension in Moon.DIMENSIONS:
                pot += abs(moon.position[dimension])
                kin += abs(moon.velocity[dimension])
            energy += pot * kin
        return energy

    def find_repeat(self):
        current_step = 0
        period_found = [False, False, False]
        periods = []
        moon_pairs = list(itertools.combinations(self.system, 2))
        while not all(period_found):
            for pair in moon_pairs:
                self.apply_gravity(pair)
            for moon in self.system:
                moon.apply_velocity()
            current_step += 1
            for i, dimension in enumerate(Moon.DIMENSIONS):
                if not period_found[i]:
                    if all([self.initial[n].position[dimension] == \
                            self.system[n].position[dimension] \
                            for n in range(4)]) and \
                        all([self.initial[n].velocity[dimension] == \
                                self.system[n].velocity[dimension] \
                                for n in range(4)]):
                        period_found[i] = True
                        periods.append(current_step)
        return self._lcm(periods)

    def _lcm(self, periods):
        [a,b,c] = periods
        lcm1 = abs(a*b) // math.gcd(a, b)
        return abs(lcm1*c) // math.gcd(lcm1, c)

class Moon:
    DIMENSIONS = ['x', 'y', 'z']
    def __init__(self, position):
        self.position = self._parse_position(position)
        self.velocity = {'x': 0, 'y': 0, 'z': 0}

    def _parse_position(self, position):
        x_pos_start = position.find('x=') + 2
        x_pos_end = position.find(',', x_pos_start)
        x_pos = int(position[x_pos_start:x_pos_end])
        y_pos_start = position.find('y=') + 2
        y_pos_end = position.find(',', y_pos_start)
        y_pos = int(position[y_pos_start:y_pos_end])
        z_pos_start = position.find('z=') + 2
        z_pos_end = position.find('>')
        z_pos = int(position[z_pos_start:z_pos_end])

        return {'x': x_pos, 'y': y_pos, 'z': z_pos}

    def apply_velocity(self):
        for dimension in Moon.DIMENSIONS:
            self.position[dimension] += self.velocity[dimension]

def partOne(puzzle_input):
    jupiter = Jupiter(puzzle_input)
    jupiter.step(1000)
    print(f"The total energy in the system is {jupiter.total_energy}.")

def partTwo(puzzle_input):
    jupiter = Jupiter(puzzle_input)
    print(f"The time to repeat is {jupiter.find_repeat()}.")

def main():
    puzzle_input = parseInput('input.txt')
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
