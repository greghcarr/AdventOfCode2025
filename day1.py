# ----- part one -----

rotations: list[str]
with open("inputs/day1.txt") as f:
    rotations = f.read().splitlines()

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

print(f'Part 1: {zeroes}')


# ----- part two -----

rotations = []
with open("inputs/day1.txt") as f:
    for line in f:
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

print(f'Part 2: {zeroes}')