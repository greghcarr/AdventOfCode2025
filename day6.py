def do_math(operator: str, operands: list):
    if operator == '+':
        return sum(operands)
    elif operator == '*':
        ret = 1
        for op in operands:
            ret *= op
        return ret

def part_one():
    # ----- part 1 -----
    
    # solution to day6test.txt: 4277556
    
    
    FILE_PATH = 'inputs/day6.txt'
    
    inputs = []
    
    with open(FILE_PATH) as f:
        for line in f:
            inputs.append(line.strip())
    
    # print(inputs)
    
    problem_matrix = [line.split() for line in inputs]
    
    sum_problems = 0
    for i in range(len(problem_matrix[0])):
        operands = []
        for j, line in enumerate(problem_matrix):
            if j == len(problem_matrix) - 1:
                operator = line[i]
            else:
                operands.append(int(line[i]))
        # print(operands)
        # print(operator)
        sum_problems += do_math(operator, operands)
    
    # print(problem_matrix)
    return sum_problems


def part_two():
    # ----- part two -----
    
    FILE_PATH = 'inputs/day6.txt'
    
    with open(FILE_PATH) as f:
        inputs = f.read().splitlines()
    
    # number = [line[-1] for line in inputs]
    
    sum_problems = 0
    operands = []
    operand_digits = []
    # i will  be our x coordinate on the problem matrix, starting on the right
    for i in range(-1, (-1 * len(inputs[0])) - 1, -1):
        # j refers to the index of the line we're on
        for j, line in enumerate(inputs):
            # if we're on one of the lines before the final line
            if j < len(inputs) - 1:
                operand_digits.append(line[i])
            # if we're on the final line, where the operators are
            if j == len(inputs) - 1:
                # finalize the operand and insert it into the operands array
                operand_string = ''.join(operand_digits).strip()
                if operand_string == '':
                    continue
                operand = int(operand_string)
                operands.append(operand)
                # if we find an operator
                if line[i] != ' ':
                    operator = line[i]
                    # send the operands and operator away to be processed and add it to the total
                    # print(f'Sending operands: {operands} with operator: {operator}')
                    sum_problems += do_math(operator, operands)
                    operands = []
                operand_digits = []
    
    return sum_problems