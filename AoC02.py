


test = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

path = 'input02.txt'


def read_txt_to_num(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            items.append(line)
    return items[0]


def retrieve_next_range(input):
    next_dash = input.find('-')
    next_comma = input.find(',')
    if next_comma < 0:
        next_comma = len(input)
    num1 = int(input[0:next_dash])
    num2 = int(input[next_dash+1:next_comma])
    return [num1, num2]


def is_invalid(n):
    num = str(n)
    if len(num) % 2 == 0:
        x = len(num)
        str1 = num[:(int(x/2))]
        str2 = num[(int(x/2)):]
        if str1 == str2:
            return True
    else:
        return False

def get_divisors(n):
    divisors = []
    for i in range(1, -(-n//2)+1):
        print(f'dividing {n} by {i}')
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_hard_invalid(n):
    num = str(n)
    l = len(num)
    divisors = get_divisors(l)
    for div in divisors:
        list_of_str = []
        for i in range(0, l, div):
            next_str = num[i:(div+i)]
            list_of_str.append(next_str)
        if len(set(list_of_str)) == 1:
            if l > 1:
                return True
    return False


def run_sum_invalids(doc):
    invalids = []
    while len(doc) > 2:
        this_range = retrieve_next_range(doc)
        print(f'range:{this_range}')
        fwd = doc.find(',')
        if fwd < 0:
            doc = ''
        else:
            doc = doc[fwd+1:]
        for this_num in range(this_range[0], this_range[1]+1):
            print(f'number {this_num}... ', end="")
            if is_invalid(this_num):
                invalids.append(this_num)
                print('invalid!')
    return invalids


def run_sum_hard_invalids(doc):
    invalids = []
    while len(doc) > 2:
        this_range = retrieve_next_range(doc)
        print(f'range:{this_range}')
        fwd = doc.find(',')
        if fwd < 0:
            doc = ''
        else:
            doc = doc[fwd + 1:]
        for this_num in range(this_range[0], this_range[1] + 1):
            print(f'number {this_num}... ', end="")
            if is_hard_invalid(this_num):
                invalids.append(this_num)
                print('invalid!')
    return invalids

    ############################
doc = read_txt_to_num(path)

inv_test1 = run_sum_invalids(test)
sum_test = sum(inv_test1)

inv_test2 = run_sum_hard_invalids(test)
sum_test2 = sum(inv_test2)


inv1 = run_sum_invalids(doc)
s1 = sum(inv1)

inv2 = run_sum_hard_invalids(doc)
s2 = sum(inv2)