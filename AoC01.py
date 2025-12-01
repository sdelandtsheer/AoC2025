### AoC 01

def rotate(start, move):
    direction = -1 if (move[0] == 'L') else 1
    distance = int(move[1:])
    to_move = direction * distance
    result = start + to_move
    while result < 0:
        result = result + 100
    while result > 99:
        result = result - 100
    return result

def make_moves_and_count_zeros(list_of_moves):
    dial = 50
    zeros = 0
    for move in list_of_moves:
        print(f'making move {move}')
        dial = rotate(dial, move)
        print(f'now at {dial}')
        if dial == 0:
            zeros += 1
    return zeros


def make_moves_any_zeros(list_of_moves):
    dial = 50
    zeros = 0
    for move in list_of_moves:
        print(f'making move {move}')
        direction = -1 if (move[0] == 'L') else 1
        distance = int(move[1:])
        for l_move in range(distance):
            this_move = move[0] + str(1)
            dial = rotate(dial, this_move)
            print(f'now at {dial}')
            if dial == 0:
                zeros += 1
    return zeros



def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items



# doc = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

doc = txt_file_to_list('input_01.txt')

rep = make_moves_and_count_zeros(doc)

rep2 = make_moves_any_zeros(doc)


