import copy
import collections

def parseInput(input):
    puzzle_input = []
    with open(input) as f:
        for line in f:
            puzzle_input.extend([int(num) for num in line.split(',')])
    return puzzle_input

class IntcodeComputer:
    def __init__(self, puzzle_input, inputs=[]):
        self.puzzle_input = copy.deepcopy(puzzle_input)
        self.puzzle_input_original = copy.deepcopy(puzzle_input)
        self.instruction_index = 0
        self.inputs = collections.deque()
        self.insertInput(inputs)
        self.inputs_original = copy.deepcopy(self.inputs)
        self.halted = False
        self.output = []
        self.relative_base = 0
        self.extra_memory = {}

    def reset(self):
        self.puzzle_input = copy.deepcopy(self.puzzle_input_original)
        self.instruction_index = 0
        self.inputs = copy.deepcopy(self.inputs_original)
        self.halted = False
        self.output = []
        self.relative_base = 0
        self.extra_memory = {}

    def insertInput(self, input):
        if type(input) == list:
            self.inputs.extend(input)
        elif type(input) == int:
            self.inputs.append(input)
        else:
            raise TypeError(f"Input must be list or int (Not {type(input)})")

    def _parameters(self, instruction_str, parameter_num, *writes):
        if parameter_num > 3:
            raise ValueError(f"Unexpected number of parameters: {parameter_num}")
        parameters = []
        for i in range(1, parameter_num + 1):
            parameter_mode = instruction_str[-2 - i]
            if i in writes:
                if parameter_mode == '0':
                    parameters.append(self._readFromIndex(
                        self.instruction_index + i))
                elif parameter_mode == '2':
                    parameters.append(
                        self._readFromIndex(self.instruction_index + i) + self.relative_base)
            else:
                if parameter_mode == '0':
                    parameters.append(self._readFromIndex(
                        self._readFromIndex(self.instruction_index + i)))
                elif parameter_mode == '1':
                    parameters.append(self._readFromIndex(
                        self.instruction_index + i))
                elif parameter_mode == '2':
                    parameters.append(self._readFromIndex(
                        self._readFromIndex(self.instruction_index + i) + self.relative_base))
        return parameters

    def _readFromIndex(self, index):
        if index < 0:
            raise IndexError(f"Negative index is not allowed: {index}")
        elif index < len(self.puzzle_input):
            return self.puzzle_input[index]
        elif index in self.extra_memory:
            return self.extra_memory[index]
        else:
            self.extra_memory[index] = 0
            return 0

    def _writeToIndex(self, index, value):
        if index < 0:
            raise IndexError(f"Negative index is not allowed: {index}")
        elif index < len(self.puzzle_input):
            self.puzzle_input[index] = value
            return
        elif index in self.extra_memory:
            self.extra_memory[index] = value
            return
        else:
            self.extra_memory[index] = value
            return

    def runCode(self):
        instruction = self._readFromIndex(self.instruction_index)
        instruction_str = '0000' + str(instruction)
        opcode = instruction_str[-2:]
        while opcode != '99':
            if opcode == '01':
                value1, value2, output_index = self._parameters(instruction_str, 3, 3)
                self._writeToIndex(output_index, value1 + value2)
                self.instruction_index += 4
            elif opcode == '02':
                value1, value2, output_index = self._parameters(instruction_str, 3, 3)
                self._writeToIndex(output_index, value1 * value2)
                self.instruction_index += 4
            elif opcode == '03':
                if len(self.inputs) == 0:
                    return self.giveOutput()
                input = self.inputs.popleft()
                [output_index] = self._parameters(instruction_str, 1, 1)
                self._writeToIndex(output_index, input)
                self.instruction_index += 2
            elif opcode == '04':
                [value1] = self._parameters(instruction_str, 1)
                self.output.append(value1)
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
                value1, value2, output_index = self._parameters(instruction_str, 3, 3)
                if value1 < value2:
                    self._writeToIndex(output_index, 1)
                else:
                    self._writeToIndex(output_index, 0)
                self.instruction_index += 4
            elif opcode == '08':
                value1, value2, output_index = self._parameters(instruction_str, 3, 3)
                if value1 == value2:
                    self._writeToIndex(output_index, 1)
                else:
                    self._writeToIndex(output_index, 0)
                self.instruction_index += 4
            elif opcode == '09':
                [value1] = self._parameters(instruction_str, 1)
                self.relative_base += value1
                self.instruction_index += 2
            else:
                raise ValueError(f'Invalid opcode: {opcode}. The instruction is {instruction_str}')
            instruction = self._readFromIndex(self.instruction_index)
            instruction_str = '0000' + str(instruction)
            opcode = instruction_str[-2:]
        return self.giveOutput()

    @property
    def isHalted(self):
        return self.halted

    def giveOutput(self):
        output, self.output = self.output, []
        if len(output) == 1:
            return output[0]
        else:
            return output

class Arcade:
    def __init__(self, puzzle_input):
        self.computer = IntcodeComputer(puzzle_input)
        self.score = 0
        self.tile_info = {}
        self.paddle = None
        self.ball = None

    def updateTileLayout(self, draw_info):
        i = 2
        while i < len(draw_info):
            if draw_info[i-2] == -1 and draw_info[i-1] == 0:
                self.score = draw_info[i]
            else:
                if draw_info[i] == 3:
                    self.paddle = (draw_info[i-2], draw_info[i-1])
                elif draw_info[i] == 4:
                    self.ball = (draw_info[i-2], draw_info[i-1])
                else:
                    self.tile_info[(draw_info[i-2], draw_info[i-1])] = draw_info[i]
            i += 3
        return

    @property
    def totalBlockTiles(self):
        return list(self.tile_info.values()).count(2)

    def startGame(self):
        self.computer.reset()
        self.computer.puzzle_input[0] = 2
        return

    def playGame(self):
        self.startGame()
        draw_info = self.computer.runCode()
        self.updateTileLayout(draw_info)
        while self.totalBlockTiles > 0 and not self.computer.isHalted:
            if self.paddle[0] < self.ball[0]:
                self.computer.insertInput(1)
            elif self.paddle[0] > self.ball[0]:
                self.computer.insertInput(-1)
            else:
                self.computer.insertInput(0)
            draw_info = self.computer.runCode()
            self.updateTileLayout(draw_info)
        if self.totalBlockTiles != 0:
            print("You lost!")
        else:
            print(f"You won! Your score is {self.score}.")


def partOne(puzzle_input):
    arcade_cabinet = Arcade(puzzle_input)
    draw_info = arcade_cabinet.computer.runCode()
    arcade_cabinet.updateTileLayout(draw_info)
    print(f"There are {arcade_cabinet.totalBlockTiles} block tiles.")


def partTwo(puzzle_input):
    arcade_cabinet = Arcade(puzzle_input)
    arcade_cabinet.playGame()

def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
