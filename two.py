import unittest


class IntMachine():

    def __init__(self, code):
        self.code = code

    def run(self):
        pos = 0
        while pos < len(self.code):
            # print(f'position {pos} {self.code[pos]} {self.code[pos] == 1}')
            if self.code[pos] == 1:
                read_one = self.code[pos + 1]
                read_two = self.code[pos + 2]
                write_pos = self.code[pos + 3]
                self.code[write_pos] = self.code[read_one] + self.code[read_two]
                pos = pos + 4
            elif self.code[pos] == 2:
                write_pos = self.code[pos + 3]
                read_one = self.code[pos + 1]
                read_two = self.code[pos + 2]
                self.code[write_pos] = self.code[read_one] * self.code[read_two]
                pos = pos + 4
            elif self.code[pos] == 99:
                return
            else:
                raise Exception(f"wrong instruction at pos: {pos} with value: {self.code[pos]}")

    @staticmethod
    def run_challenge(part):
        ints = open("inputs/two.txt").readline().split(',')
        code = [int(x) for x in ints]
        if part == 'a':
            code[1] = 12
            code[2] = 2
            machine = IntMachine(code)
            machine.run()
            print(machine.code)
        else:
            for noun in range(0, 100):
                for verb in range(0, 100):
                    # print(f'{noun} {verb}')
                    temp_code = code.copy()
                    temp_code[1] = noun
                    temp_code[2] = verb
                    machine = IntMachine(temp_code)
                    machine.run()
                    if machine.code[0] == 19690720:
                        print(f'noun: {noun} verb {verb} result: {100 * noun + verb}')
                        return


class DayTwo(unittest.TestCase):

    def test_simple_op(self):
        sut = IntMachine([1, 0, 0, 3])
        sut.run()
        self.assertEqual([1, 0, 0, 2], sut.code)

    def test_advanced_op(self):
        code = [1, 9, 10, 3,
                2, 3, 11, 0,
                99,
                30, 40, 50]
        sut = IntMachine(code)
        sut.run()
        self.assertEqual([3500, 9, 10, 70,
                          2, 3, 11, 0,
                          99,
                          30, 40, 50], sut.code)

    def test_more_ops(self):
        code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        sut = IntMachine(code)
        sut.run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], sut.code)


if __name__ == '__main__':
    unittest.main()
