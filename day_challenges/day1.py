import helpers.input_reader as ir

FILE_PATH = 'input/day1.txt'
# ----- part one -----

def part_one():
    global pos
    rotations = ir.read_file(FILE_PATH)

    # print(rotations)

    pos = 50
    zeroes = 0

    for rot in rotations:
        if rot[0] == 'R':
            pos += int(rot[1:])
        elif rot[0] == 'L':
            pos -= int(rot[1:])
        if pos % 100 == 0:
            zeroes += 1

    return zeroes

# ----- part two -----

def part_two():
    global pos
    inputs = ir.read_file(FILE_PATH)
    rotations = []
    for line in inputs:
        rotations.append(int(line.strip().replace('L', '-').replace('R', '')))

    # print(rotations)

    pos = 50
    zeroes = 0

    for rotation in rotations:
        rotation = int(rotation)
        if rotation > 0:
            for i in range(rotation):
                pos += 1
                if pos % 100 == 0: zeroes += 1
        elif rotation < 0:
            for i in range(abs(rotation)):
                pos -= 1
                if pos % 100 == 0: zeroes += 1

    return zeroes