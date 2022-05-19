count = int(input())
for i in range(count):
    row, col = map(int, input().split())
    ls1 = []
    ls2 = []
    ls3 = []

    for j in range(row):
        li = list(map(int, input().split()))
        ls1.append(li)
    for k in range(row):
        li = list(map(int, input().split()))
        ls2.append(li)

    for a in range(row):
        ls3 = []
        for b in range(col):
            sum_ = 0
            sum_ += ls1[a][b] * ls2[a][b]
            ls3.append(sum_)
        for c in range(len(ls3)):
            print(ls3[c], end=' ')
        print('')


