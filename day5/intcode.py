import copy

def parseInput(input):
    input_numbers = []
    with open(input) as f:
        for line in f:
            input_numbers.extend([int(num) for num in line.split(',')])
    return input_numbers

def intCodeAdvanced(puzzle_input, input=1):
    instruction_index = 0
    output = []
    instruction = puzzle_input[instruction_index]
    instruction_str = '0000' + str(instruction)
    opcode = instruction_str[-2:]
    while opcode != '99' and instruction_index < len(puzzle_input) - 2:
        if instruction_str[-3] == '0':
            value1 = puzzle_input[puzzle_input[instruction_index + 1]]
        elif instruction_str[-3] == '1':
            value1 = puzzle_input[instruction_index + 1]
        if opcode in ['01', '02', '05', '06', '07', '08']:
            if instruction_str[-4] == '0':
                value2 = puzzle_input[puzzle_input[instruction_index + 2]]
            elif instruction_str[-4] == '1':
                value2 = puzzle_input[instruction_index + 2]
            if opcode in ['01', '02', '07', '08']:
                output_index = puzzle_input[instruction_index + 3]
        if opcode == '01':
            puzzle_input[output_index] = value1 + value2
            instruction_index += 4
        elif opcode == '02':
            puzzle_input[output_index] = value1 * value2
            instruction_index += 4
        elif opcode == '03':
            puzzle_input[puzzle_input[instruction_index + 1]] = input
            instruction_index += 2
        elif opcode == '04':
            output.append(value1)
            instruction_index += 2
        elif opcode == '05':
            if value1 != 0:
                instruction_index = value2
            else:
                instruction_index += 3
        elif opcode == '06':
            if value1 == 0:
                instruction_index = value2
            else:
                instruction_index += 3
        elif opcode == '07':
            if value1 < value2:
                puzzle_input[output_index] = 1
            else:
                puzzle_input[output_index] = 0
            instruction_index += 4
        elif opcode == '08':
            if value1 == value2:
                puzzle_input[output_index] = 1
            else:
                puzzle_input[output_index] = 0
            instruction_index += 4
        else:
            raise ValueError(f'Invalid opcode: {opcode}. The instruction is {instruction_str}')
        instruction = puzzle_input[instruction_index]
        instruction_str = '0000' + str(instruction)
        opcode = instruction_str[-2:]
    return puzzle_input, output

def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    input_copy = copy.deepcopy(puzzle_input)
    final_puzzle, output = intCodeAdvanced(input_copy)
    print(f'The output is {output}')
    input_copy_2 = copy.deepcopy(puzzle_input)
    final_puzzle_2, output_2 = intCodeAdvanced(input_copy_2, 5)
    print(f'The output is {output_2}')

if __name__ == '__main__':
    main()
