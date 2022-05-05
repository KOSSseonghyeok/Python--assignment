count = int(input())
for i in range(count):
    h, m = map(int, input().split())
    h = h * 30 + m / 2
    m = (m/5)*30
    sum_ = abs(h - m)
    if sum_ > 180:
        sum_ = 360 - sum_
    print(int(sum_))
