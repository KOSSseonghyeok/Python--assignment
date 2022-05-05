t = int(input())

for i in range(t):
    num = int(input())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    print(li[0], li[-1])
    li.clear()



