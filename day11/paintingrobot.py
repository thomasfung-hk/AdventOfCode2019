import copy

def parseInput(input):
    puzzle_input = []
    with open(input) as f:
        for line in f:
            puzzle_input.extend([int(num) for num in line.split(',')])
    return puzzle_input

class IntcodeComputer:
    def __init__(self, puzzle_input, inputs=[]):
        self.puzzle_input = copy.deepcopy(puzzle_input)
        self.instruction_index = 0
        self.inputs = []
        self.insertInput(inputs)
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
                input = self.inputs.pop(0)
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

class PaintingRobot:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    def __init__(self, puzzle_input):
        self.position = (0,0)
        self.direction = PaintingRobot.UP
        self.board = {}
        self.computer = IntcodeComputer(puzzle_input)

    def paint_board(self, starting_panel):
        while not self.computer.isHalted:
            if self.position not in self.board:
                if self.position == (0,0):
                    self.computer.insertInput(starting_panel)
                else:
                    self.computer.insertInput(0)
            else:
                self.computer.insertInput(self.board[self.position])
            try:
                instructions = self.computer.runCode()
                paint_color, turn_direction = instructions
            except ValueError:
                return
            self.board[self.position] = paint_color
            if turn_direction == 0:
                self.direction = (self.direction - 1) % 4
            elif turn_direction == 1:
                self.direction = (self.direction + 1) % 4
            else:
                raise ValueError(f"Invalid turn direction: {turn_direction}")
            if self.direction == PaintingRobot.UP:
                self.position = (self.position[0], self.position[1] + 1)
            elif self.direction == PaintingRobot.RIGHT:
                self.position = (self.position[0] + 1, self.position[1])
            elif self.direction == PaintingRobot.DOWN:
                self.position = (self.position[0], self.position[1] - 1)
            elif self.direction == PaintingRobot.LEFT:
                self.position = (self.position[0] - 1, self.position[1])
            else:
                raise ValueError(f"Invalid direction: {self.direction}")
        return

    @property
    def painted_panels(self):
        return len(self.board)

    def limits(self):
        y_upper = 0
        y_lower = 0
        x_upper = 0
        x_lower = 0
        for (x, y) in self.board.keys():
            if y > y_upper:
                y_upper = y
            if y < y_lower:
                y_lower = y
            if x > x_upper:
                x_upper = x
            if x < x_lower:
                x_lower = x
        return((x_lower, x_upper),(y_lower, y_upper))

    def visualize(self):
        BLACK_PANEL = '■'
        WHITE_PANEL = '□'
        (x_range, y_range) = self.limits()
        x_dimension = x_range[1] - x_range[0] + 3
        y_dimension = y_range[1] - y_range[0] + 3
        for y in range(y_dimension):
            row = ''
            for x in range(x_dimension):
                coordinates = (x-1,1-y)
                if coordinates not in self.board:
                    row += BLACK_PANEL
                else:
                    if self.board[coordinates] == 0:
                        row += BLACK_PANEL
                    else:
                        row += WHITE_PANEL
            print(row)
        return

def partOne(puzzle_input):
    robot = PaintingRobot(puzzle_input)
    robot.paint_board(0)
    print(f"There are {robot.painted_panels} panels that are painted at least once.")

def partTwo(puzzle_input):
    robot = PaintingRobot(puzzle_input)
    robot.paint_board(1)
    robot.visualize()

def main():
    filename = "input.txt"
    puzzle_input = parseInput(filename)
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
