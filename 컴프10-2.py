def foo(fix, ls, k):
    if k == 0:
        if fix[k + 1] <= 2 or fix[k + 1] >= 8:
            if ls[k] != 0:
                ls[k] -= 1
        elif fix[k + 1] > 3:
            if fix[k] != 9:
                ls[k] += 1
    elif k == len(ls)-1:
        if fix[k - 1] <= 2 or fix[k - 1] >= 8:
            if ls[k] != 0:
                ls[k] -= 1
        elif fix[k - 1] > 3:
            if fix[k] != 9:
                ls[k] += 1
    else:
        if fix[k + 1] + fix[k - 1] <= 2 or fix[k + 1] + fix[k - 1] >= 8:
            if ls[k] != 0:
                ls[k] -= 1
        elif fix[k + 1] + fix[k - 1] > 3:
            if fix[k] != 9:
                ls[k] += 1

count = int(input())
for i in range(count):
    num, cnt = map(int, input().split())
    ls = list(map(int, input().split()))
    for j in range(cnt):
        fix = ls[:]
        for k in range(len(ls)):
            foo(fix, ls, k)
    for a in ls:
        print(a, end=' ')
    print()
