
test = ['7,1',
        '11,1',
        '11,7',
        '9,7',
        '9,5',
        '2,5',
        '2,3',
        '7,3']


def txt_file_to_list(path_or_test):
    items = []
    if isinstance(path_or_test, str):
        with open(path_or_test, "r", encoding="utf-8") as f:
            for line in f:
                comma = line.find(',')
                l = int(line[:comma])
                c = int(line[comma+1:])
                items.append((l, c))
    else:
        for line in path_or_test:
            comma = line.find(',')
            l = int(line[:comma])
            c = int(line[comma + 1:])
            items.append((l, c))

    return items

def compute_area(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    area = (abs(l2-l1)+1) * (abs(c2-c1)+1)
    return area

def compute_largest_area(input):
    max_area = 1
    coord = ()
    for p1 in input:
        print(f'starting top left: {p1}')
        for p2 in input:
            print(f'trying bottom right: {p2}')
            area = compute_area(p1, p2)
            if area > max_area:
                print(f'better area: {area} at {p1, p2}')
                max_area = area
                coord = (p1, p2)
    return max_area, coord



def area_largest_rectangle(path_or_test):
    input = txt_file_to_list(path_or_test)
    area, coord = compute_largest_area(input)

    return area, coord

def compute_largest_full_area(filled_input):
    max_area = 1
    coord = ()
    for p1 in input:
        print(f'starting top left: {p1}')
        for p2 in input:
            print(f'trying bottom right: {p2}')
            area = compute_area(p1, p2)
            if area > max_area:
                # check if full
                if is_full(p1, p2, filled_input):
                    print(f'better area: {area} at {p1, p2}')
                    max_area = area
                    coord = (p1, p2)
    return max_area, coord


def is_full(p1, p2, filled_input):
    full = True
    l1, c1 = p1
    l2, c2 = p2
    for l in range(min(l1, l2), max(l1, l2)):
        for c in range(min(c1, c2), max(c1, c2)):
            if (l, c) not in filled_input:
                full = False
    return full

def filling_input(input):
    greens = []
    for p1 in input:
        for p2 in input:
            print(f'acting on {p1} and {p2}')
            if p1 != p2:
                l1, c1 = p1
                l2, c2 = p2
                if l1 == l2:
                    c_left = min(c1, c2)
                    c_right = max(c1, c2)
                    for fill in range(c_left, c_right):
                        greens.append((l1, fill))
                        print(f'appending {(l1, fill)}')
                elif c1 == c2:
                    l_high = min(l1, l2)
                    l_low = max(l1, l2)
                    for fill in range(l_high, l_low):
                        greens.append((fill, c1))
                        print(f'appending {(fill, c1)}')
    for i in range(int(1E5)):
        for j in range(int(1E5)):
            print(f'screening point {i, j}')
            if (i, j) not in greens and (i, j) not in input:
                high = [x for x in input if (x[0] == i and x[1]<j)]
                low = [x for x in input if (x[0] == i and x[1]>j)]
                left = [x for x in input if (x[1] == i and x[0]<j)]
                right = [x for x in input if (x[1] == i and x[0]>j)]
                if len(right) * len(left) * len(low) * len(high) > 0:
                    greens.append(i, j)

    return greens

def area_largest_full_rectangle(path_or_test):
    input = txt_file_to_list(path_or_test)
    filled_input = filling_input(input)
    area, coord = compute_largest_full_area(filled_input)



s1_test, coordinates = area_largest_rectangle(test)
print(f'largest: {s1_test} ({coordinates})')

s1, coordinates = area_largest_rectangle('input_09.txt')
print(f'largest: {s1} ({coordinates})')

s2_test, coordinates = area_largest_full_rectangle(test)
print(f'largest: {s2_test} ({coordinates})')
