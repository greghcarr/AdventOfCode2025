# ----- part 1 -----

# solution to day7test.txt: 21

def print_lines(lines: List[int]) -> None:
    for l in lines:
        print(l)

def part_one():
    FILE_PATH = 'inputs/day7.txt'
    
    inputs = []
    
    with open(FILE_PATH) as f:
        for line in f:
            inputs.append(line.strip())
    
    # print_lines(inputs)
    
    splits = 0
    
    # for each line after the first
    for line_index, line in enumerate(inputs[1:]):
        # print(list(line))
        # for each character on the line
        for char_index, char in enumerate(line):
            # if the character on the above line at the same index is an 'S' or a '|'
            if inputs[line_index - 1][char_index] == '|' or inputs[line_index - 1][char_index] == 'S':
                # if the current character is a splitter
                if char == '^':
                    # turn the line into a list
                    line_list = list(line)
                    # change the preceding and proceeding chars to '|'
                    line_list[char_index - 1] = '|'
                    line_list[char_index + 1] = '|'
                    # turn the list back into the line
                    line = ''.join(line_list)
                    inputs[line_index] = line
                    # print(line)
                    # increment the split count
                    splits += 1
                # if the current character isn't a splitter
                else:
                    # change the current character to '|'
                    line_list = list(line)
                    line_list[char_index] = '|'
                    line = ''.join(line_list)
                    inputs[line_index] = line
                    
    # print_lines(inputs)
    return splits

# ----- part 2 -----

def part_two():
    FILE_PATH = 'inputs/day7.txt'
    diagram = []
    with open(FILE_PATH) as f:
        for line in f:
            diagram.append(line.strip())
            
    return None