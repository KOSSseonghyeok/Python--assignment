'''import math
total = int(input())
count = 0
li = [int(x) for x in range(100) if x%2 != 0]
for n in range(total):
    if count <= int(total/2):
        if li.index(total) % 2 == 0:
            print('0'*math.ceil(((total-count)/2))+"1"*count+'0'*int(((total-count)/2)))
            count += 1
        else:
            print('1' * math.ceil(((total - count) / 2)) + "0" * count + '1' * int(((total - count) / 2)))
            count += 1
    else:
        count = 0
        if li.index(total) % 2 == 0:
            print('0'*math.ceil(((total-count)/2))+"1"*count+'0'*int(((total-count)/2)))
            count += 1
        else:
            print('1' * math.ceil(((total - count) / 2)) + "0" * count + '1' * int(((total - count) / 2)))
            count += 1'''

def square(n):
    if n > 0:
        li = [int(x) for x in range(100) if x%2 != 0]
        if li.index(n) % 2 == 0:
            print('0'*n, end='')


            return square(n - 2)
    else:

