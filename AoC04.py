# Day 4

import numpy as np


test = ['..@@.@@@@.',
       '@@@.@.@.@@',
        '@@@@@.@.@@',
        '@.@@@@..@.',
        '@@.@@@@.@@',
        '.@@@@@@@.@',
        '.@.@.@.@@@',
        '@.@@@.@@@@',
        '.@@@@@@@@.',
        '@.@.@@@.@.']


def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items


def make_matrix(input):
    ar = []
    l = len(input[0])
    for line in input:
        row = [1 if roll=='@' else 0 for roll in line]
        ar.append(row)
    return np.array(ar)

def run_count_rolls(array):
    result = np.zeros_like(array)
    pad_array = np.pad(array, pad_width=1, mode='constant', constant_values=0)
    kernel = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]])

    for i in range(pad_array.shape[0] - 2):
        for j in range(pad_array.shape[1] - 2):
            focus = pad_array[i:min(i+3, pad_array.shape[0]), j:min(j+3, pad_array.shape[1])]
            result[i, j] = np.sum(focus * kernel)

    return result

def process_stack(array):
    sums = run_count_rolls(array)
    result = array.copy()
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 1:
                if sums[i, j] < 4:
                    result[i, j] = 0
    return result


test_matrix = make_matrix(test)
sums = run_count_rolls(test_matrix)
s_test = np.sum((sums<4) & (test_matrix>0))

v1 = txt_file_to_list('input_04.txt')
s1_matrix = make_matrix(v1)
sums_s1 = run_count_rolls(s1_matrix)
s1 = np.sum((sums_s1<4) & (s1_matrix>0))

total_rolls = 0
need_process = True
matrix = s1_matrix
while need_process:
    sums = run_count_rolls(matrix)
    this_sum = np.sum((sums<4)&(matrix>0))
    print(this_sum)
    total_rolls += this_sum
    if this_sum == 0:
        need_process = False
    else:
        matrix = process_stack(matrix)

