
# ----- part one -----
with open('inputs/day2.txt') as f:
    ranges = f.read().split(',')

# print(ranges)

invalid_ids = []

for r in ranges:
    begin, end = r.split('-')
    # print(begin, end)
    for i in range(int(begin), int(end)+1):
        if len(str(i)) % 2 == 0:
            midpoint = int(len(str(i))/2)
            if str(i)[0:midpoint] == str(i)[midpoint:len(str(i))]:
                invalid_ids.append(i)

# print(invalid_ids)
print(f'Part one sum: {sum(invalid_ids)}')


# ----- part two -----
from functools import reduce

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

with open('inputs/day2.txt') as f:
    ranges = f.read().split(',')

# print(ranges)

invalid_ids = []

for r in ranges:
    begin, end = r.split('-')
    # print(begin, end)
    # for i, each number in the range
    for i in range(int(begin), int(end)+1):
        # for j, each factor of the length of i
        for j in factors(len(str(i))):
            # except the length itself (e.g. 1, 2, and 3 for i=6 but not 6 itself)
            if j != len(str(i)):
                # try replacing the substring of length j starting at zero with nothing
                # if you're left with nothing, it's an invalid id
                if str(i).replace(str(i)[0:j],'') == '':
                    if i not in invalid_ids:
                        invalid_ids.append(i)

# print(f'Part two ids: {invalid_ids}')
print(f'Part two sum: {sum(invalid_ids)}')

