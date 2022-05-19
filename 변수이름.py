count = int(input())
for i in range(count):
    name = input()
    li = []
    for j in name:
        li.append(j)
    if li[0].isalpha():
        for k in range(1, len(li)):
            if li[k].isalpha() == 0 and li[k].isdigit() == 0:
                if li[k] == '_':
                    continue
                else:
                    print(0)
                    break
        else:
            print(1)
    else:
        if li[0] == "_":
            for k in range(1, len(li)):
                if li[k].isalpha() == 0 and li[k].isdigit() == 0:
                    if li[k] == '_':
                        continue
                    else:
                        print(0)
                        break
            else:
                print(1)
        else:
            print(0)