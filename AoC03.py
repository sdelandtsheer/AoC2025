# day 3

test = [987654321111111,
        811111111111119,
        234234234234278,
        818181911112111]

SORTED_DIGITS = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']


def largest_digits(bank, n=2):
    instr = str(bank)
    l = len(instr)
    pos = 0
    needed = n
    all_digits = []

    while needed > 0:
        last_start = l - needed
        window = instr[pos:last_start+1]

        for s in SORTED_DIGITS:
            idx = window.find(s)
            if idx > -1:
                actual_idx = pos + idx
                all_digits.append(s)
                pos = actual_idx + 1
                needed -= 1
                break
    return int(''.join(all_digits))


def run_and_sum_banks(path, n=2):
    if not isinstance(path, list):
        input = txt_file_to_list(path)
    else:
        input = path
    running_sum = 0
    for this_bank in input:
        l = largest_digits(this_bank, n)
        print(l)
        running_sum += l
    return running_sum



def txt_file_to_list(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line.rstrip("\n"))
    return items



path = 'input_03.txt'
stest = run_and_sum_banks(test, n=2)
s1 = run_and_sum_banks(path, n=2)
s2test = run_and_sum_banks(test, n=12)
s2 = run_and_sum_banks(path, n=12)
