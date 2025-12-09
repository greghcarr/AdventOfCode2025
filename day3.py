def part_one():
    # day3test.txt solution: 98 + 89 + 78 + 92 = 357

    FILE_PATH = 'inputs/day3.txt'

    with open(FILE_PATH) as f:
        inputs = f.read().splitlines()

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
    FILE_PATH = 'inputs/day3.txt'

    with open(FILE_PATH) as f:
        inputs = f.read().splitlines()

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