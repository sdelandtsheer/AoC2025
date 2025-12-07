

test = ['123 328  51 64',
        '45 64  387 23',
        '6 98  215 314',
        '*   +   *   +']

def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items

def extract_num(line):
    next_space = line.find(' ')
    if next_space < 0:
        return int(line), None
    this_num = int(line[:next_space])
    line = line[next_space:]
    while line[0] == ' ':
        line = line[1:]
    return this_num, line

def extract_sign(line):
    next_space = line.find(' ')
    if next_space < 0:
        return line, None
    this_sign = line[:next_space]
    line = line[next_space:]
    while line[0] == ' ':
        line = line[1:]
    return this_sign, line

def str_to_arrays(input):
    arrays = []
    for rep in range(len(input) - 1):
        num, line = extract_num(input[rep])
        x = [num]
        while line:
            num, line = extract_num(line)
            if num is not None:
                x.append(num)
        arrays.append(x)

    sign, line = extract_sign(input[-1])
    x = [sign]
    while line:
        sign, line = extract_sign(line)
        if sign is not None:
            x.append(sign)

    arrays.append(x)

    return arrays

def process_and_sum_arrays(arrays):
    lengths = [len(x) for x in arrays]
    n_arrays = len(arrays)
    all_eq = len(set(lengths)) == 1
    total = 0
    temps = []
    if not all_eq:
        print('not all arrays have the same length')
        return
    l = lengths[0]
    for i in range(l):
        numbers = [arrays[x][i] for x in range(n_arrays-1)]
        sign = arrays[-1][i]
        if sign == '+':
            temp = sum(numbers)
        elif sign == '*':
            temp = numbers[0]
            for ii in numbers[1:]:
                temp = temp * ii
        temps.append(temp)
        total += temp

    return total, temps

###chatGPT because I am lasy but curious
def solve_part2(lines):
    """
    Compute the Part 2 grand total for the cephalopod math sheet.

    - We read the grid column-by-column, left to right (right-to-left is equivalent
      because + and * are commutative/associative).
    - The bottom row contains + or * operators, or spaces.
    - Every column's digits above the bottom row form ONE vertical number.
    - When we see an operator in the bottom row, we:
        * finalize the previous running result into `total`
        * switch the current operator
        * reset the running result to the neutral element of that operator
          (0 for '+', 1 for '*').
    - For every column (including operator columns), if it has digits above,
      we build the integer and apply the current operator with that number.
    """

    # Make sure everything is a string, avoids 'list has no attribute ljust' etc.
    lines = [str(row) for row in lines]

    H = len(lines)
    if H == 0:
        return 0

    # Pad all rows on the right so indexing is safe for all columns
    W = max(len(row) for row in lines)
    grid = [row.ljust(W) for row in lines]

    # Bottom row is where the operators live
    operators_row = grid[-1]

    total = 0  # Grand total across all problems
    current = 0  # Running result for the "current" group of columns
    operator = '+'  # Current operator (will be overwritten at first symbol)

    for idx in range(W):
        op_char = operators_row[idx]

        # If there's an operator in this column, we first close the previous group
        if op_char in ('+', '*'):
            # Add the result of the previous group to the total
            total += current

            # Switch to the new operator
            operator = op_char

            # Reset current to the identity of that operator
            current = 1 if operator == '*' else 0

        # Collect digits from this column (all rows except the last operator row)
        digits = []
        for r in range(H - 1):
            ch = grid[r][idx]
            if ch.isdigit():
                digits.append(ch)

        # If this column actually had a number, apply it
        if digits:
            num = int("".join(digits))
            if operator == '*':
                current *= num
            else:  # operator == '+'
                current += num

    # Don't forget to flush the last group
    total += current

    return total


input_test = test
arrays_test = str_to_arrays(input_test)

s_test, temps = process_and_sum_arrays(arrays_test)

input = txt_file_to_list('input_06.txt')
arrays_1 = str_to_arrays(input)

s1, temps = process_and_sum_arrays(arrays_1)

s2 = solve_part2(input)