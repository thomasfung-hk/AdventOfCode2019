import copy

def parseInput(input):
    input_numbers = []
    with open(input) as f:
        for line in f:
            input_numbers.extend([int(num) for num in line.split(',')])
    return input_numbers

def gravityProgram(puzzle_input):
    opcode_index = 0
    while puzzle_input[opcode_index] != 99 and opcode_index < len(puzzle_input) - 4:
        opcode = puzzle_input[opcode_index]
        value1 = puzzle_input[puzzle_input[opcode_index + 1]]
        value2 = puzzle_input[puzzle_input[opcode_index + 2]]
        output_index = puzzle_input[opcode_index + 3]
        if opcode == 1:
            puzzle_input[output_index] = value1 + value2
        elif opcode ==2:
            puzzle_input[output_index] = value1 * value2
        else:
            raise ValueError(f'Invalid opcode: {opcode}')
        opcode_index += 4
    return puzzle_input

def nounVerbFinder(puzzle_input, target):
    for noun in range(100):
        for verb in range(100):
            input_copy = copy.deepcopy(puzzle_input)
            input_copy[1] = noun
            input_copy[2] = verb
            zero_pos_val = gravityProgram(input_copy)[0]
            if zero_pos_val == target:
                return(noun, verb)
    return(0, 0)


def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    input_copy = copy.deepcopy(puzzle_input)
    input_copy[1] = 12
    input_copy[2] = 2
    final_state = gravityProgram(input_copy)
    print(f"After the program halts, the 0 position holds the value {final_state[0]}.")
    (noun, verb) = nounVerbFinder(puzzle_input, 19690720)
    print(f"The noun is {noun} and the verb is {verb} that cause the program to\
 produce the output 19690720. The answer is {100 * noun + verb}.")

if __name__ == '__main__':
    main()
