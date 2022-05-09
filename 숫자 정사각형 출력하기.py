num = int(input())
ls = []
ls2 = []
a = 0

li = [int(k) for k in range(1, 100) if k % 2 != 0]
for i in range(num):
    count = int(input())
    if li.index(count) % 2 != 0:
        for j in range(int((count+1)/2)):
            if ls == []:
                for c in range(int(count)):
                    ls.append("1")
                ls2.insert(a, ''.join(ls))
                a += 1

            else:
                if ls[a] == "1":
                    for u in range(a, count-a):
                        ls[u] = "0"
                else:
                    for u in range(a, count-a):
                        ls[u] = "1"
                ls2.insert(a, ''.join(ls))
                a += 1
        ls = []
        a = 0
        b = 0
        while b < (count+1)/2:
            print(ls2[b])
            b += 1
        b = 1
        ls2 = ls2[::-1]
        while b < (count+1)/2:
            print(ls2[b])
            b += 1
        ls2 = []
    else:
        for j in range(int((count + 1) / 2)):
            if ls == []:
                for c in range(int(count)):
                    ls.append("0")
                ls2.insert(a, ''.join(ls))
                a += 1

            else:
                if ls[a] == "1":
                    for u in range(a, count - a):
                        ls[u] = "0"
                else:
                    for u in range(a, count - a):
                        ls[u] = "1"
                ls2.insert(a, ''.join(ls))
                a += 1
        ls = []
        a = 0
        b = 0
        while b < (count + 1) / 2:
            print(ls2[b])
            b += 1
        b = 1
        ls2 = ls2[::-1]
        while b < (count + 1) / 2:
            print(ls2[b])
            b += 1
        ls2 = []