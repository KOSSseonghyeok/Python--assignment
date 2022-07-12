GREGORIAN = 1582
li = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(y, m, d):
    sum_ = 0
    is_leap = lambda n: (n % 4 == 0 and n % 100 != 0) or n % 400 == 0
    for n in range(GREGORIAN, y):
        sum_ += 365 + int(is_leap(n))
    li[2] = 29 if is_leap(y) else 28
    sum_ += sum(li[:m]) + d
    print((sum_ + 4) % 7)
count = int(input())
for _ in range(0, count):
    solution(*list(map(int, input().split())))