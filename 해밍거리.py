count = int(input())
for i in range(count):
    ls = list(map(int, input().split()))
    for k in range(len(ls)):
        ls[k] = bin(ls[k])
        ls[k] = str(ls[k])
    li = []
    for j in ls:
        count = 0
        j = j[2:]
        for k in j:
            if k == '1':
                count += 1
        li.append(count)
    cnt = 0
    a = ls[0][2:]
    b = ls[1][2:]
    if len(a) > len(b):
        b = "0"*(len(a)-len(b)) + b
    elif len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    for l in range(len(a)):
        if a[l] != b[l]:
           cnt += 1
    li.append(cnt)
    for m in li:
        print(m, end=' ')
    print()

