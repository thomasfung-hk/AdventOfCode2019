import math

def parseInput(input):
    puzzle_input = []
    with open(input) as f:
        for line in f:
            puzzle_input.append(line.strip())
    return puzzle_input

class Chemical:
    def __init__(self, reaction):
        self._parse_reaction(reaction)

    def _parse_reaction(self, reaction):
        chemicals_needed = reaction[:reaction.index(" => ")].split(", ")
        end_product = reaction[reaction.index(" => ") + 4:]
        self.formula = {}
        for item in chemicals_needed:
            num, chemical = item.split(" ")
            self.formula[chemical] = int(num)
        end_product_details = end_product.split(" ")
        self.unit_per_formula = int(end_product_details[0])
        self.name = end_product_details[1]

    @property
    def chemicals_needed(self):
        return list(self.formula.keys())

class Nanofactory:
    def __init__(self, puzzle_input):
        self.chemical_master = {'ORE': None}
        self.resource_master = {'ORE': 0}
        self.ore_used = 0
        for reaction in puzzle_input:
            chemical = Chemical(reaction)
            self.chemical_master[chemical.name] = chemical
            self.resource_master[chemical.name] = 0

    def make_chemical(self, chemical, num):
        if chemical == 'ORE':
            self.resource_master['ORE'] += num
            self.ore_used += num
            return
        target_chemical = self.chemical_master[chemical]
        formula = target_chemical.formula
        formula_times = math.ceil(num / target_chemical.unit_per_formula)
        for chemical_needed in target_chemical.chemicals_needed:
            units_needed = formula_times * formula[chemical_needed]
            if self.resource_master[chemical_needed] >= units_needed:
                self.resource_master[chemical_needed] -= units_needed
            else:
                extra_units_needed = units_needed - self.resource_master[chemical_needed]
                self.make_chemical(chemical_needed, extra_units_needed)
                self.resource_master[chemical_needed] -= units_needed
        self.resource_master[chemical] += formula_times * target_chemical.unit_per_formula
        return

    def ore_for_fuel(self, fuel_needed):
        self.reset()
        self.make_chemical('FUEL', fuel_needed)
        return self.ore_used

    def reset(self):
        for key in self.resource_master.keys():
            self.resource_master[key] = 0
        self.ore_used = 0

def partOne(puzzle_input):
    factory = Nanofactory(puzzle_input)
    return factory.ore_for_fuel(1)

def partTwo(puzzle_input):
    ore_deposit = 1000000000000
    factory = Nanofactory(puzzle_input)
    lower_limit = 1
    upper_limit = 2
    while factory.ore_for_fuel(upper_limit) < ore_deposit:
        lower_limit *= 2
        upper_limit *= 2
    i = lower_limit + (upper_limit - lower_limit) // 2
    while upper_limit - lower_limit > 1:
        ore_needed = factory.ore_for_fuel(i)
        if ore_needed < ore_deposit:
            lower_limit = i
        elif ore_needed > ore_deposit:
            upper_limit = i
        else:
            return i
        i = lower_limit + (upper_limit - lower_limit) // 2
    return lower_limit


def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    print(f"In order to generate 1 FUEL, {partOne(puzzle_input)} ORE is needed.")
    print(f"Given 1 trillion ORE, {partTwo(puzzle_input)} FUEL can be produced.")

if __name__ == '__main__':
    main()
