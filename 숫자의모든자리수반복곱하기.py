count = int(input())
sum_ = 1
for i in range(count):
    num = input()
    while len(num) > 1:
        for j in num:
            if int(j) != 0:
                sum_ *= int(j)
            else:
                continue
        num = str(sum_)
        if len(num) != 1:
            sum_ = 1
    print(sum_)
    sum_ = 1



