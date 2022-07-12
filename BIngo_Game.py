count = int(input())
for i in range(count):
    ls = []
    li = []
    for j in range(5):
        ls = list(map(int, input().split()))
        li.append(ls)
    num = list(map(int, input().split()))
    for k in num:
        sum_ = 0
        for m in range(5):
            for n in range(5):
                if li[m][n] == k:
                    li[m][n] = 0
        b = 1
        while b < 6:
            for c in range(5):
                if li[c][b-1] != 0:
                    break
            else:
                sum_ = num.index(k) + 1
                print(sum_)
                b = 6
            if sum_ == 0:
                b += 1
        if sum_ != 0:
            break
        d = 1
        while d < 6:
            for e in range(5):
                if li[d-1][e] != 0:
                    break
            else:
                sum_ = num.index(k) + 1
                print(sum_)
                d = 6
            if sum_ == 0:
                d += 1
        if sum_ != 0:
            break
        f = 1
        while f < 6:
            for g in range(5):
                if li[g][g] != 0:
                    f = 6
                    break
            else:
                sum_ = num.index(k) + 1
                print(sum_)
                f = 6
        if sum_ != 0:
            break
        h = 1
        while h < 6:
            for v in range(5):
                if li[v][4-v] != 0:
                    h = 6
                    break
            else:
                sum_ = num.index(k) + 1
                print(sum_)
                h = 6
        if sum_ != 0:
            break
        ls2 = [0, 4]
        for s in ls2:
            for r in ls2:
                if li[s][r] != 0:
                    break
                if li[r][r] != 0:
                    break
                if li[r][s] != 0:
                    break
            else:
                sum_ = num.index(k) + 1
                print(sum_)
            break
        if sum_ != 0:
            break













