import helpers.input_reader as ir

FILE_PATH = 'input/day3.txt'

def part_one():
    # day3test.txt solution: 98 + 89 + 78 + 92 = 357

    inputs = ir.read_file(FILE_PATH)

    joltages = []
    for seq in inputs:
        first_digit = seq[0]
        first_digit_index = 0
        # check only to the second to last digit
        for i in range(len(seq) - 1):
            if seq[i] > first_digit:
                first_digit = seq[i]
                first_digit_index = i
        second_digit = seq[first_digit_index + 1]
        for j in range(first_digit_index + 1, len(seq)):
            if seq[j] > second_digit:
                second_digit = seq[j]
        joltage = int(f'{first_digit}{second_digit}')
        joltages.append(joltage)

    return sum(joltages)

# ----- part 2 -----

def part_two():
    inputs = ir.read_file(FILE_PATH)

    joltages = []
    for seq in inputs:
        last_digit_index = -1
        joltage_digits = []
        for h in range(11, -1, -1):
            digit = 0
            for i in range(last_digit_index + 1, len(seq) - h):
                if int(seq[i]) > digit:
                    digit = int(seq[i])
                    last_digit_index = i
            joltage_digits.append(str(digit))
        joltages.append(int(''.join(joltage_digits)))

    # print(f'Joltages: {joltages}')
    return sum(joltages)