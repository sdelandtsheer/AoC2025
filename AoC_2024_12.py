### 2024 Day 12 ###

test = ['RRRRIICCFF', 'RRRRIICCCF', 'VVRRRCCFFF', 'VVRCCCJFFF', 'VVVVCJJCFE', 'VVIVCCJJEE', 'VVIIICJJEE', 'MIIIIIJJEE', 'MIIISIJEEE', 'MMMISSJEEE']

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, x):
        self.queue.append(x)

    def get(self):
        x = self.queue[0]
        self.queue = self.queue[1:]
        return x

    def size(self):
        return len(self.queue)


def neighbors(input, i, j):
    max_i = len(input)
    max_j = len(input[0])
    n = []
    if i > 0:
        n.append((i-1, j))
    if j > 0:
        n.append((i, j-1))
    if i < max_i:
        n.append((i+1, j))
    if j < max_j:
        n.append((i, j+1))
    return n




def search(input, i, j):
    visited = [(i, j)]
    q = Queue()
    q.add((i, j))
    nature = input[i][j]
    all_pos = [(i, j)]

    while q.queue:
        i, j = q.get()
        n_list = neighbors(input, i, j)
        for n in n_list:
            if n not in visited:
                visited.append(n)
                if input[n[0]][n[1]] == nature:
                    q.add(n)
                    all_pos.append(n)

    return all_pos


def compute_fence(region):
    area = len(region)


def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items

x = search(test, 0, 0)