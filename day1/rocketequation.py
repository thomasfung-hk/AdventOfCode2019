import math

def parseInput(input):
    input_numbers = []
    with open(input) as f:
        for line in f:
            input_numbers.extend([int(num) for num in line.split()])

    return input_numbers

def fuelCalculator(module_list):
    total_fuel = 0
    for mass in module_list:
        fuel = math.floor(mass/3) - 2
        total_fuel += fuel

    return total_fuel

def fuelCalculator2(module_list):
    total_fuel = 0
    for mass in module_list:
        while True:
            fuel = math.floor(mass/3) - 2
            if fuel > 0:
                total_fuel += fuel
                mass = fuel
            else:
                break

    return total_fuel

def main():
    filename = "input.txt"
    module_list = parseInput(filename)
    total_fuel = fuelCalculator(module_list)
    print(f"Fuel required is {total_fuel}")

    total_fuel_2 = fuelCalculator2(module_list)
    print(f"Upon double checking, fuel required is {total_fuel_2}")

if __name__ == '__main__':
    main()
