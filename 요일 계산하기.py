count = int(input())

li = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for j in range(count):
    ls = list(map(int, input().split()))
    sum_ = 0
    for n in range(1, ls[0]):
        if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
            sum_ += 366
        else:
            sum_ += 365

    if (ls[0] % 4 == 0 and ls[0] % 100 != 0) or ls[0] % 400 == 0:
        for i in range(1, ls[1]):
            sum_ += li[i]

    else:
        for i in range(1, ls[1]):
            if li[i] == 29:
                li[i] = 28
            sum_ += li[i]

    sum_ += ls[2]
    print(sum_ % 7)




