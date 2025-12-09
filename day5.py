def get_fresh_id_ranges(input: List[str]) -> List[Tuple[int, int]]:
    return [tuple(int(s) for s in line.split('-')) for line in input if '-' in line]

def get_available_ids(input: List[str]) -> List[int]:
    available_ids = []
    for line in input:
        if '-' not in line and line.strip() != '':
            available_ids.append(int(line))
    return available_ids

def get_num_ints_in_ranges(ints: List[int], ranges: List[Tuple[int, int]]) -> int:
    num_ints_in_ranges = 0
    ints_in_ranges = []
    for n in ints:
        for r in ranges:
            if r[0] <= n <= r[1] and n not in ints_in_ranges:
                num_ints_in_ranges += 1
                ints_in_ranges.append(n)
    return num_ints_in_ranges

def part_one() -> Any:
    # ----- part 1 -----

    # solution to day5test.txt: 3

    FILE_PATH = 'inputs/day5.txt'

    with open(FILE_PATH) as f:
        inputs = f.read().splitlines()

    fresh_id_ranges = get_fresh_id_ranges(inputs)
    available_ids = get_available_ids(inputs)

    num_fresh_available_ids = get_num_ints_in_ranges(available_ids, fresh_id_ranges)

    return num_fresh_available_ids


def part_two():
    global start, end
    # ----- part 2 -----

    FILE_PATH = 'inputs/day5.txt'

    with open(FILE_PATH) as f:
        inputs = f.read().splitlines()

    fresh_id_ranges = get_fresh_id_ranges(inputs)

    # sort ranges by starting value
    sorted_ranges = sorted(fresh_id_ranges)

    num_ints_in_ranges = 0
    cur_start, cur_end = sorted_ranges[0]
    for start, end in sorted_ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            num_ints_in_ranges += (cur_end - cur_start + 1)
            cur_start, cur_end = start, end
    num_ints_in_ranges += (cur_end - cur_start + 1)

    return num_ints_in_ranges
