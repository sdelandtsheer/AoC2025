### Day 8

test = ['162,817,812',
        '57,618,57',
        '906,360,560',
        '592,479,940',
        '352,342,300',
        '466,668,158',
        '542,29,236',
        '431,825,988',
        '739,650,466',
        '52,470,668',
        '216,146,977',
        '819,987,18',
        '117,168,530',
        '805,96,715',
        '346,949,466',
        '970,615,88',
        '941,993,340',
        '862,61,35',
        '984,92,344',
        '425,690,689']


def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            c = line.find(',')
            x = int(line[:c])
            line = line[c+1:]
            c = line.find(',')
            y = int(line[:c])
            z = int(line[c+1:])
            items.append((x, y, z))
    return items

def test_to_list(test):
    items = []
    for line in test:
        c = line.find(',')
        x = int(line[:c])
        line = line[c + 1:]
        c = line.find(',')
        y = int(line[:c])
        z = int(line[c + 1:])
        items.append((x, y, z))
    return items



def euclidian(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dz = abs(z1 - z2)
    dist = (dx*dx + dy*dy + dz*dz) ** 0.5

    return dist

def make_dist_matrix(input):
    L = len(input)
    matrix = [[-1 for i in range(L)] for j in range(L)]
    for l in range(L):
        a = input[l]
        for c in range(L):
            if matrix[l][c] < 0:
                b = input[c]
                d = euclidian(a, b)
                matrix[l][c] = d
                matrix[c][l] = d
    for l in range(L):
        matrix[l][l] = 1E6
    return matrix

def find_closest(matrix, input, n_links):
    result = []
    n_connect = 0
    ceiling = max(max(matrix))
    while n_connect < n_links:
        mins_per_line = [min(line) for line in matrix]
        bottom = min(mins_per_line)
        print(f'new low: {bottom}')

        l_find = mins_per_line.index(bottom)
        c_find = matrix[l_find].index(bottom)
        print(f'coordinates: {l_find}, {c_find}')
        print(f'id: {input[l_find]}, {input[c_find]}')
        matrix[l_find][c_find] = ceiling
        matrix[c_find][l_find] = ceiling

        found = [-1, -1]
        for idx, group in enumerate(result):
            if l_find in group:
                print(f'{input[l_find]} exists in {group}')
                found[0] = idx
            if c_find in group:
                print(f'{input[c_find]} exists in {group}')
                found[1] = idx

        print(found)
        if found == [-1, -1]:
            print(f'new group: {input[l_find]}, {input[c_find]}')
            n_connect += 1
            result.append([l_find, c_find])
            print(f'result: {result}')
        elif (found[1] < 0) and (found[0] >= 0):
            print(f'{input[l_find]} exists in {result[found[0]]}')
            result[found[0]].append(c_find)
            n_connect += 1
        elif (found[0] < 0) and (found[1] >= 0):
            print(f'{input[c_find]} exists in {result[found[1]]}')
            result[found[1]].append(l_find)
            n_connect += 1
        elif (found[0] * found[1]) >= 0:
            if found[0] == found[1]:
                print(f'{input[l_find]} and {input[c_find]} exist in {result[found[0]]}')
                n_connect += 1
                # pass
            else:
                print(f'{input[l_find]} and {input[c_find]} exist in {result[found[0]]} and {result[found[1]]}')
                merged = list(set(result[found[0]] + result[found[1]]))
                result[found[0]] = merged
                result.pop(found[1])
                n_connect += 1
        print(result)

    return result


def count_largest_groups(input=input, n_links=None, n_groups=None):
    matrix = make_dist_matrix(input)
    result = find_closest(matrix, input, n_links)
    lengths = [len(x) for x in result]
    to_multiply = sorted(lengths, reverse=True)[:n_groups]
    total = 1
    for i in to_multiply:
        total = total * i

    return total, result

def part2(input):
    is_all_connected = False
    matrix = make_dist_matrix(input)
    result = []
    n_connect = 0
    ceiling = max(max(matrix))
    while not is_all_connected:
        mins_per_line = [min(line) for line in matrix]
        bottom = min(mins_per_line)
        print(f'new low: {bottom}')

        l_find = mins_per_line.index(bottom)
        c_find = matrix[l_find].index(bottom)
        print(f'coordinates: {l_find}, {c_find}')
        print(f'id: {input[l_find]}, {input[c_find]}')
        matrix[l_find][c_find] = ceiling
        matrix[c_find][l_find] = ceiling

        found = [-1, -1]
        for idx, group in enumerate(result):
            if l_find in group:
                print(f'{input[l_find]} exists in {group}')
                found[0] = idx
            if c_find in group:
                print(f'{input[c_find]} exists in {group}')
                found[1] = idx

        print(found)
        if found == [-1, -1]:
            print(f'new group: {input[l_find]}, {input[c_find]}')
            n_connect += 1
            result.append([l_find, c_find])
            print(f'result: {result}')
        elif (found[1] < 0) and (found[0] >= 0):
            print(f'{input[l_find]} exists in {result[found[0]]}')
            result[found[0]].append(c_find)
            n_connect += 1
        elif (found[0] < 0) and (found[1] >= 0):
            print(f'{input[c_find]} exists in {result[found[1]]}')
            result[found[1]].append(l_find)
            n_connect += 1
        elif (found[0] * found[1]) >= 0:
            if found[0] == found[1]:
                print(f'{input[l_find]} and {input[c_find]} exist in {result[found[0]]}')
                n_connect += 1
                # pass
            else:
                print(f'{input[l_find]} and {input[c_find]} exist in {result[found[0]]} and {result[found[1]]}')
                merged = list(set(result[found[0]] + result[found[1]]))
                result[found[0]] = merged
                result.pop(found[1])
                n_connect += 1
        print(result)
        if (len(result) == 1) and (len(result[0]) == len(input)):
            is_all_connected = True

    x1, y1, z1 = input[l_find]
    x2, y2, z2 = input[c_find]

    return (x1 * x2)





input = test_to_list(test)
n_links = 10
n_groups = 3
s1_test, groups = count_largest_groups(input, n_links=n_links, n_groups=n_groups)
print(s1_test)

input = txt_file_to_list('input_08.txt')
n_links = 1000
s1, groups = count_largest_groups(input, n_links=n_links, n_groups=n_groups)

s2 = part2(input)