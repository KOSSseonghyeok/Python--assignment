count = int(input())
for i in range(count):
    num = 0
    li = []
    ls = list(map(int, input().split()))
    for j in range(len(ls)):
        if ls[j] not in li:
            li.append(ls[j])
        elif li[-1] != ls[j]:
            li.append(ls[j])
        else:
            continue
    for k in range(1, len(li)-1):
        if li[k-1] < li[k] and li[k+1] < li[k]:
            num += 1
    print(num)
