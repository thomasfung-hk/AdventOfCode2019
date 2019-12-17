import math

def parseInput(input):
    return open(input).readline().strip()

class FFT:
    def __init__(self, puzzle_input):
        self.original = puzzle_input[:]
        self.currentlist = puzzle_input
        self.inputlength = len(puzzle_input)
        self.patterns = self.makePatterns()
        self.phase = 0
        self.digit_sum = self.sumOfDigits()

    def sumOfDigits(self):
        return sum(int(digit) for digit in self.currentlist)

    def makePatterns(self):
        patterns = {}
        for n in range(1, self.inputlength + 1):
            repetitions = math.ceil((self.inputlength + 1) / (4 * n))
            pattern_long = ([0] * n + [1] * n + [0] * n + [-1] * n) * repetitions
            patterns[n] = pattern_long[1:self.inputlength + 1]
        return patterns

    def reset(self):
        self.currentlist = self.original[:]
        self.phase = 0

    def runCalculations(self, phase):
        if self.phase > phase:
            self.reset()
        while self.phase < phase:
            output = 0
            for output_digit_place in range(1, self.inputlength + 1):
                acc = 0
                pattern = self.patterns[output_digit_place]
                for ind, input_digit in enumerate(self.currentlist):
                    acc += int(input_digit) * pattern[ind]
                output = 10*output + (abs(acc) % 10)
            self.currentlist = '0' * (self.inputlength - len(str(output))) + str(output)
            self.phase += 1
        return self.currentlist

    def runCalculations_10000(self):
        self.reset()
        offset = int(self.currentlist[:7])
        if offset + 8 > self.inputlength * 10000:
            print("The offset exceeds the length of the input (times 10000).")
            return
        total_digits = self.inputlength * 10000
        actual_digits = total_digits - offset
        snippit =  ''
        for ind in range(total_digits - 1, offset - 1, -1):
            digit = self.currentlist[ind % self.inputlength]
            snippit = digit + snippit
        phase = 0
        while phase < 100:
            new_snippit = ''
            acc = 0
            for i in range(actual_digits - 1, -1, -1):
                acc = (acc + int(snippit[i])) % 10
                new_snippit = str(acc) + new_snippit
            snippit = new_snippit
            phase += 1
            print(f"Phase {phase}...")
        return snippit[:8]


def partOne(puzzle_input):
    fft_algo = FFT(puzzle_input)
    print(f"The first eight digits in the final output list is {fft_algo.runCalculations(100)[:8]}.")

def partTwo(puzzle_input):
    fft_algo = FFT(puzzle_input)
    print(f"The message in the final output list is {fft_algo.runCalculations_10000()}.")

def main():
    puzzle_input = parseInput('input.txt')
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
