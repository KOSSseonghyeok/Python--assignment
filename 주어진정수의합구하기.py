count = int(input())
sum_ = 0
for i in range(count):
    num = int(input())
    li = list(map(int, input().split()))
    for j in range(num):
        sum_ += li[j]
    print(sum_)
    sum_ = 0