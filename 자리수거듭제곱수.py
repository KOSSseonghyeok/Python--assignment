count = int(input())
for j in range(count):
    num = input()
    length = len(num)
    sum_ = 0
    for i in num:
        sum_ += int(i)**length
    if int(num) == sum_:
        print(1)
    else:
        print(0)

