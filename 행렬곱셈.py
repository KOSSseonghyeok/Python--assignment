def mk(ls1, ls2, r, s, t):
    for j in range(r):
        ls1.append(list(map(int, input().split())))
    for b in range(s):
        ls2.append(list(map(int, input().split())))

count = int(input())
for i in range(count):
    ls1 = []
    ls2 = []
    fix = []
    r, s, t = map(int, input().split())
    mk(ls1, ls2, r, s, t)
    for k in range(r):
        for m in range(t):
            sum_ = 0
            for l in range(s):
                sum_ += ls1[k][l]*ls2[l][m]
            fix.append(sum_)
    cnt = 0
    for a in fix:
        print(a, end=' ')
        cnt += 1
        if cnt == t:
            cnt = 0
            print()



