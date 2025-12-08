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

def find_closest(matrix, n_links):
    result = [[]]
    n_connect = 0
    ceiling = max(max(matrix))
    while n_connect < n_links:
        bottom = min(min(matrix))
        print(f'new low: {bottom}')
        l_find = min(matrix).index(bottom)
        if not isinstance(l_find, int):
            l_find = l_find[0]
        c_find = matrix[l_find].index(bottom)
        if not isinstance(c_find, int):
            c_find = c_find[0]
        print(f'coordinates: {l_find}, {c_find}')
        matrix[l_find][c_find] = ceiling
        matrix[c_find][l_find] = ceiling

        found = False
        for res in result:
            if l_find in res and c_find in res:
                print(f'both {l_find} and {c_find} exist in {res}')
                found = True
                break
            elif l_find in res:
                print(f'{l_find} already in {res}, adding {c_find}')
                res.append(c_find)
                n_connect += 1
                found = True
                break
            elif c_find in res:
                print(f'{c_find} already in {res}, adding {l_find}')
                res.append(l_find)
                n_connect += 1
                found = True
                break
        if not found:
            print(f'new')
            n_connect += 1
            result.append([l_find, c_find])
            print(f'result: {result}')

    return result

def count_largest_groups(input=input, n_links=None, n_groups=None):
    matrix = make_dist_matrix(input)
    result = find_closest(matrix, n_links)
    lengths = [len(x) for x in result]
    to_multiply = sorted(lengths, reverse=True)[:n_groups]
    total = 1
    for i in to_multiply:
        total = total * i

    return total, result







input = test_to_list(test)
n_links = 10
n_groups = 3
s1_test, groups = count_largest_groups(input, n_links=n_links, n_groups=n_groups)
print(s1_test)

