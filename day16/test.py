import unittest
import fft

class DaysSixteenTest(unittest.TestCase):
    def test_pattern_1(self):
        fft_algo = fft.FFT('12345678')
        self.assertEqual(fft_algo.patterns[1], [1, 0, -1, 0, 1, 0, -1, 0])
        self.assertEqual(fft_algo.patterns[2], [0, 1, 1, 0, 0, -1, -1, 0])

    def test_phase_1(self):
        fft_algo = fft.FFT('12345678')
        self.assertEqual(fft_algo.runCalculations(1), '48226158')
        self.assertEqual(fft_algo.runCalculations(2), '34040438')
        self.assertEqual(fft_algo.runCalculations(3), '03415518')
        self.assertEqual(fft_algo.runCalculations(4), '01029498')

    def test_phase_2(self):
        fft_algo = fft.FFT('80871224585914546619083218645595')
        self.assertEqual(fft_algo.runCalculations(100)[:8], '24176176')

    def test_phase_3(self):
        fft_algo = fft.FFT('19617804207202209144916044189917')
        self.assertEqual(fft_algo.runCalculations(100)[:8], '73745418')

    def test_phase_4(self):
        fft_algo = fft.FFT('69317163492948606335995924319873')
        self.assertEqual(fft_algo.runCalculations(100)[:8], '52432133')

    def test_long_1(self):
        fft_algo = fft.FFT('03036732577212944063491565474664')
        self.assertEqual(fft_algo.runCalculations_10000(), '84462026')

    def test_long_2(self):
        fft_algo = fft.FFT('02935109699940807407585447034323')
        self.assertEqual(fft_algo.runCalculations_10000(), '78725270')

    def test_long_3(self):
        fft_algo = fft.FFT('03081770884921959731165446850517')
        self.assertEqual(fft_algo.runCalculations_10000(), '53553731')

if __name__ == '__main__':
    unittest.main()
