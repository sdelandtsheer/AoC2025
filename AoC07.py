

test =['.......S.......',
       '...............',
       '.......^.......',
       '...............',
       '......^.^......',
       '...............',
       '.....^.^.^.....',
       '...............',
       '....^.^...^....',
       '...............',
       '...^.^...^.^...',
       '...............',
       '..^...^.....^..',
       '...............',
       '.^.^.^.^.^...^.',
       '...............']


def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items


def prune(array):
    new_array = []
    for line in array:
        if set(line) != {'.'}:
            new_array.append(line)
    return new_array


def has_beam(clean_input, l, c, active_beams):
    if (l, c) in active_beams:
        return True
    current_line = l
    while 1:
        current_line -= 1
        x = clean_input[current_line][c]
        if x == 'S':
            return True
        elif x == '^':
            return False
        elif x == '.':
            if clean_input[current_line][c - 1] == '^':
                left_beam = has_beam(clean_input, current_line, c - 1, active_beams)
            else:
                left_beam = False
            if clean_input[current_line][c + 1] == '^':
                right_beam = has_beam(clean_input, current_line, c + 1, active_beams)
            else:
                right_beam = False
            if left_beam or right_beam:
                return True



def count_splits(input):
    active_beams = []
    current = 0
    clean_input = prune(input)
    L = len(clean_input)
    C = len(clean_input[0])
    for l in range(L):
        for c in range(C):
            if clean_input[l][c] == '^':
                if has_beam(clean_input, l, c, active_beams):
                    print(f'beam active in {l, c}')
                    current += 1
                    active_beams.append((l, c))
                else:
                    print(f'no beam for {l, c}')
    return current






input = test
s_test = count_splits(input)
print(f'test: {s_test}')

input = txt_file_to_list('input_07.txt')
s1 = count_splits(input)
print(f'1: {s1}')

s2 = enumerate_paths(input)
print(f's2: {s2}')


