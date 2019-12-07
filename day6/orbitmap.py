def parseInput(input):
    orbitfile = open(input, 'r')
    return [line.strip() for line in orbitfile.readlines()]

def main():
    filename = "input.txt"
    orbit_info = parseInput(filename)
    planet_wiki = PlanetCollection()
    planet_wiki.process(orbit_info)
    print(f'There are {planet_wiki.totalOrbits} total orbits')
    print(f'You need {planet_wiki.transfers("YOU", "SAN")} orbital transfers to get to Santa')

class PlanetCollection:
    def __init__(self):
        self.collection = {}

    def addOrbit(self, orbit):
        planets = orbit.split(")")
        if planets[0] in self.collection:
            parent = self.collection[planets[0]]
        else:
            parent = Planet(planets[0])
            self.collection[planets[0]] = parent
        if planets[1] in self.collection:
            child = self.collection[planets[1]]
        else:
            child = Planet(planets[1])
            self.collection[planets[1]] = child
        child.addParent(parent)

    @property
    def totalOrbits(self):
        orbit_count = 0
        all_planets = list(self.collection.values())
        for planet in all_planets:
            orbit_count += planet.orbits
        return orbit_count

    def process(self, orbit_info):
        for orbit in orbit_info:
            self.addOrbit(orbit)

    def transfers(self, planet_1, planet_2):
        path_1 = self.collection[planet_1].parentOrbits
        path_2 = self.collection[planet_2].parentOrbits
        for i, planet in enumerate(path_1):
            if planet in path_2:
                return i + path_2.index(planet)
        raise ValueError('No common parent found!')

class Planet:
    def __init__(self, name):
        self.orbits = 0
        self.name = name
        self.parent = None

    def addParent(self, parent):
        self.parent = parent
        planet = parent
        while planet:
            planet.orbits += self.orbits + 1
            planet = planet.parent

    @property
    def parentOrbits(self):
        parents = []
        planet = self.parent
        while planet:
            parents.append(planet.name)
            planet = planet.parent
        return parents


if __name__ == '__main__':
    main()
