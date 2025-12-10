import helpers.input_reader as ir

FILE_PATH = 'input/day4.txt'

def part_one():
    # ----- part 1 -----

    # solution to day4test.txt: 13
    
    inputs = ir.read_file(FILE_PATH)

    accessible_rolls = 0

    # for each line
    for i, line in enumerate(inputs):
        # for each char in each line
        for j, char in enumerate(line):
            # we're going to count the adjacent rolls, initialize the variable
            adjacent_rolls = 0
            # if the char we're looking at is a roll
            if char == '@':
                # left, only look if we are not at the beginning of the line
                if j - 1 >= 0 and line[j - 1] == '@':
                    adjacent_rolls += 1
                # right, only look if we're not at the end of the line
                if j + 1 < len(line) and line[j + 1] == '@':
                    adjacent_rolls += 1

                # top left, only look if we are not at the beginning of the line and not on the first line
                if j - 1 >= 0 and i > 0 and inputs[i - 1][j - 1] == '@':
                    adjacent_rolls += 1
                # top middle, only check if we are not on the first line
                if i > 0 and inputs[i - 1][j] == '@':
                    adjacent_rolls += 1
                # top right, only check if we are not on the first line and not at the end of the line
                if j + 1 < len(line) and i > 0 and inputs[i - 1][j + 1] == '@':
                    adjacent_rolls += 1

                # bottom left, only check if we are not at the beginning of a line and not on the last line
                if j - 1 >= 0 and i < len(inputs) - 1 and inputs[i + 1][j - 1] == '@':
                    adjacent_rolls += 1
                # bottom middle, only check if we are not on the last line
                if i < len(inputs) - 1 and inputs[i + 1][j] == '@':
                    adjacent_rolls += 1
                # bottom right, only check if we are not on the last line and not at the end of a line
                if i < len(inputs) - 1 and j + 1 < len(line) and inputs[i + 1][j + 1] == '@':
                    adjacent_rolls += 1

                # print(f'Line {i}, char {j}, adjacent rolls: {adjacent_rolls}')

                if adjacent_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls


def part_two():
    # ----- part 2 -----

    inputs = ir.read_file(FILE_PATH)

    def delete_rolls(lines: List[str], positions: List[Tuple[int, int]]) -> List[str]:
        for position in positions:
            line_as_list = list(lines[position[0]])
            line_as_list[position[1]] = '.'
            lines[position[0]] = ''.join(line_as_list)
        return lines

    def find_accessible_rolls(lines: List[str]) -> List[Tuple[int, int]]:
        accessible_rolls = []
        # for each line
        for i, line in enumerate(lines):
            # for each char in each line
            for j, char in enumerate(line):
                # we're going to count the adjacent rolls, initialize the variable
                adjacent_rolls = 0
                # if the char we're looking at is a roll
                if char == '@':
                    # left, only look if we are not at the beginning of the line
                    if j - 1 >= 0 and line[j - 1] == '@':
                        adjacent_rolls += 1
                    # right, only look if we're not at the end of the line
                    if j + 1 < len(line) and line[j + 1] == '@':
                        adjacent_rolls += 1

                    # top left, only look if we are not at the beginning of the line and not on the first line
                    if j - 1 >= 0 and i > 0 and inputs[i - 1][j - 1] == '@':
                        adjacent_rolls += 1
                    # top middle, only check if we are not on the first line
                    if i > 0 and inputs[i - 1][j] == '@':
                        adjacent_rolls += 1
                    # top right, only check if we are not on the first line and not at the end of the line
                    if j + 1 < len(line) and i > 0 and inputs[i - 1][j + 1] == '@':
                        adjacent_rolls += 1

                    # bottom left, only check if we are not at the beginning of a line and not on the last line
                    if j - 1 >= 0 and i < len(inputs) - 1 and inputs[i + 1][j - 1] == '@':
                        adjacent_rolls += 1
                    # bottom middle, only check if we are not on the last line
                    if i < len(inputs) - 1 and inputs[i + 1][j] == '@':
                        adjacent_rolls += 1
                    # bottom right, only check if we are not on the last line and not at the end of a line
                    if i < len(inputs) - 1 and j + 1 < len(line) and inputs[i + 1][j + 1] == '@':
                        adjacent_rolls += 1

                    # print(f'Line {i}, char {j}, adjacent rolls: {adjacent_rolls}')

                    if adjacent_rolls < 4:
                        accessible_rolls.append((i, j))
        return accessible_rolls

    removed_rolls = 0
    accessible_rolls = find_accessible_rolls(inputs)
    while len(accessible_rolls) > 0:
        removed_rolls += len(accessible_rolls)
        inputs = delete_rolls(inputs, accessible_rolls)
        accessible_rolls = find_accessible_rolls(inputs)

    return removed_rolls
