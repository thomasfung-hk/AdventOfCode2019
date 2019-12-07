import copy
from itertools import permutations

def parseInput(input):
    input_numbers = []
    with open(input) as f:
        for line in f:
            input_numbers.extend([int(num) for num in line.split(',')])
    return input_numbers

class Amplifier:
    def __init__(self, puzzle_input, inputs=[]):
        self.puzzle_input = copy.deepcopy(puzzle_input)
        self.instruction_index = 0
        self.inputs = []
        self.insertInput(inputs)
        self.halted = False
        self.output = None

    def insertInput(self, input):
        if type(input) == list:
            self.inputs.extend(input)
        elif type(input) == int:
            self.inputs.append(input)
        else:
            raise TypeError(f"Input must be list or int (Not {type(input)})")

    def _parameters(self, instruction_str, parameter_num):
        if instruction_str[-3] == '0':
            value1 = self.puzzle_input[self.puzzle_input[self.instruction_index + 1]]
        elif instruction_str[-3] == '1':
            value1 = self.puzzle_input[self.instruction_index + 1]
        if parameter_num == 1:
            return value1
        if instruction_str[-4] == '0':
            value2 = self.puzzle_input[self.puzzle_input[self.instruction_index + 2]]
        elif instruction_str[-4] == '1':
            value2 = self.puzzle_input[self.instruction_index + 2]
        if parameter_num == 2:
            return value1, value2
        output_index = self.puzzle_input[self.instruction_index + 3]
        if parameter_num == 3:
            return value1, value2, output_index
        return ValueError(f"Unexpected number of parameters: {parameter_num}")

    def runCode(self):
        instruction = self.puzzle_input[self.instruction_index]
        instruction_str = '0000' + str(instruction)
        opcode = instruction_str[-2:]
        while opcode != '99' and self.instruction_index < len(self.puzzle_input) - 2:
            if opcode == '01':
                value1, value2, output_index = self._parameters(instruction_str, 3)
                self.puzzle_input[output_index] = value1 + value2
                self.instruction_index += 4
            elif opcode == '02':
                value1, value2, output_index = self._parameters(instruction_str, 3)
                self.puzzle_input[output_index] = value1 * value2
                self.instruction_index += 4
            elif opcode == '03':
                if len(self.inputs) == 0:
                    if self.output is not None:
                        output, self.output = self.output, None
                        return output
                    else:
                        raise ValueError("Output not found")
                input = self.inputs.pop(0)
                self.puzzle_input[self.puzzle_input[self.instruction_index + 1]] = input
                self.instruction_index += 2
            elif opcode == '04':
                if self.output is not None:
                    raise ValueError(f"Multiple output values detected; self.output = {self.output}")
                value1 = self._parameters(instruction_str, 1)
                self.output = value1
                self.instruction_index += 2
            elif opcode == '05':
                value1, value2 = self._parameters(instruction_str, 2)
                if value1 != 0:
                    self.instruction_index = value2
                else:
                    self.instruction_index += 3
            elif opcode == '06':
                value1, value2 = self._parameters(instruction_str, 2)
                if value1 == 0:
                    self.instruction_index = value2
                else:
                    self.instruction_index += 3
            elif opcode == '07':
                value1, value2, output_index = self._parameters(instruction_str, 3)
                if value1 < value2:
                    self.puzzle_input[output_index] = 1
                else:
                    self.puzzle_input[output_index] = 0
                self.instruction_index += 4
            elif opcode == '08':
                value1, value2, output_index = self._parameters(instruction_str, 3)
                if value1 == value2:
                    self.puzzle_input[output_index] = 1
                else:
                    self.puzzle_input[output_index] = 0
                self.instruction_index += 4
            else:
                raise ValueError(f'Invalid opcode: {opcode}. The instruction is {instruction_str}')
            instruction = self.puzzle_input[self.instruction_index]
            instruction_str = '0000' + str(instruction)
            opcode = instruction_str[-2:]
        if self.output is not None:
            output, self.output = self.output, None
            self.halted = True
            return output
        else:
            raise ValueError("Output not found")

    @property
    def isHalted(self):
        return self.halted

    def finalSignal(self):
        if self.output:
            return self.output
        else:
            raise ValueError("Output not found")

def bestPhaseSetting(puzzle_input):
    phase_settings = permutations([0,1,2,3,4])
    best_sequence = None
    best_signal = -float('Inf')
    for phases in phase_settings:
        signal = 0
        for phase in phases:
            amplifier = Amplifier(puzzle_input, [phase, signal])
            signal = amplifier.runCode()
        if signal > best_signal:
            best_signal = signal
            best_sequence = phases
    return best_sequence, best_signal

def partOne(puzzle_input):
    best_sequence, best_signal = bestPhaseSetting(puzzle_input)
    print(f'Max thruster signal {best_signal} (from phase setting sequence {best_sequence})')

def amplifierLoop(puzzle_input, phases):
    amplifiers = [Amplifier(puzzle_input, phase) for phase in phases]
    signal = 0
    amplifier_index = 0
    while not(amplifiers[amplifier_index].isHalted):
        amplifiers[amplifier_index].insertInput(signal)
        signal = amplifiers[amplifier_index].runCode()
        amplifier_index += 1
        if amplifier_index == 5:
            amplifier_index = 0
    return signal

def bestPhaseSetting_loop(puzzle_input):
    phase_settings = permutations([5,6,7,8,9])
    best_sequence = None
    best_signal = -float('Inf')
    for phases in phase_settings:
        for phase in phases:
            signal = amplifierLoop(puzzle_input, phases)
        if signal > best_signal:
            best_signal = signal
            best_sequence = phases
    return best_sequence, best_signal

def partTwo(puzzle_input):
    best_sequence, best_signal = bestPhaseSetting_loop(puzzle_input)
    print(f'Max thruster signal {best_signal} (from phase setting sequence {best_sequence})')


def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
