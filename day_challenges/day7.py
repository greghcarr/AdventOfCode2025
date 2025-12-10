import helpers.input_reader as ir

FILE_PATH = 'input/day7.txt'

# ----- part 1 -----

# solution to day7test.txt: 21

def print_lines(lines: List[int]) -> None:
    for l in lines:
        print(l)

def part_one():
    
    inputs = ir.read_file(FILE_PATH)
    
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
    diagram = ir.read_file(FILE_PATH)
            
    paths_matrix = []
    
    for line_index, line in enumerate(diagram):
        # print(f'Line #: {line_index}')
        # make the paths_line all zeroes
        paths_line = [0 for _ in range(len(line))]
        for char_index, char in enumerate(line):
            # for the first line only, find the source(s)
            if line_index == 0:
                if char == 'S':
                    paths_line[char_index] = 1
            else:
                # if no splitter
                if char == '.':
                    # add number above
                    paths_line[char_index] += (paths_matrix[line_index - 1][char_index])
                # if splitter
                if char == '^':
                    # add above to spaces to the left and right of current
                    paths_line[char_index - 1] += paths_matrix[line_index - 1][char_index]
                    paths_line[char_index + 1] += paths_matrix[line_index - 1][char_index]
        paths_matrix.append(paths_line)
    # sum of the last line of the paths matrix is the answer
    return sum(paths_matrix[len(paths_matrix) - 1])
                    
            
                
                
            
    return None