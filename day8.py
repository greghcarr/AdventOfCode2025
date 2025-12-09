import math

def read_inputs(file_path: str) -> list[str]:
    inputs = []
    with open(file_path) as f:
        for line in f:
            inputs.append(line.strip())
    return inputs

def print_lines(lines: list[str]):
    for line in lines:
        print(line)
        

FILE_PATH = 'inputs/day8test.txt'

class Day8:
    def __init__(self):

        self.inputs = read_inputs(FILE_PATH)

        # print_lines(self.inputs)
        


