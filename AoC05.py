# Day 5

test = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']

def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items

def explicitate_ranges(input):
    ranges_start = []
    ranges_stop = []
    for line in input:
        print(line)
        if '-' in line:
            splitted = line.split('-')
            start = int(splitted[0])
            finish = int(splitted[1])
            ranges_start.append(start)
            ranges_stop.append(finish)

    return ranges_start, ranges_stop


def run_and_count_fresh(input):
    fresh_start, fresh_stop = explicitate_ranges(input)
    n = 0
    for line in input:
        if '-' not in line and line != '':
            num = int(line)
            for i in range(len(fresh_start)):
                if fresh_start[i] <= num <= fresh_stop[i]:
                    print(f'{fresh_start[i]} <= {num} <= {fresh_stop[i]}')
                    n += 1
                    break

    return n

# def numerate_all_fresh(input):
#     fresh_start, fresh_stop = explicitate_ranges(input)
#     maximum = max(max(fresh_start), max(fresh_stop))
#     n = 0
#     for num in range(maximum):
#         if num % 1000 == 0:
#             print(num)
#         for i in range(len(fresh_start)):
#             if fresh_start[i] <= num <= fresh_stop[i]:
#                 print(f'{fresh_start[i]} <= {num} <= {fresh_stop[i]}')
#                 n += 1
#                 break
    ### too slow


def merge_ranges(starts, stops):
    ranges = [(s, e) for s, e in zip(starts, stops)]
    ranges.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = ranges[0]

    for new_start, new_end in ranges[1:]:
        if new_start <= current_end + 1:  # if overlapping or touching
            current_end = max(current_end, new_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = new_start, new_end

    merged.append((current_start, current_end))  # last range
    return merged


def numerate_all_fresh(input):
    fresh_start, fresh_stop = explicitate_ranges(input)
    merged = merge_ranges(fresh_start, fresh_stop)

    total = 0
    for start, stop in merged:
        total += (stop - start + 1)
    return total


input1 = txt_file_to_list('input_05.txt')

s_test = run_and_count_fresh(test)

s1 = run_and_count_fresh(input1)

s2 = numerate_all_fresh(input1)
