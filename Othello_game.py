def foo(total, col, raw):
    if total[col][raw] == "X":
        if total[col - 1][raw] == "O":
            if total[col + 1][raw] == "O":
                total[col][raw] == "O"
            elif total[col + 1][raw] == "X":
                for b in range(9-col):
                    if total[col + b][raw] == "O":
                        for c in range(b+1):
                            total[col + c][raw] == "O"
                        break

        if total[col + 1][raw] == "O":
            if total[col - 1][raw] == "O":
                total[col][raw] == "O"
            elif total[col - 1][raw] == "X":
                for b in range(9-col):
                    if total[col - b][raw] == "O":
                        for c in range(b+1):
                            total[col - c][raw] == "O"
                        break

        if total[col][raw + 1] == "O":
            if total[col][raw - 1] == "O":
                total[col][raw] == "O"
            elif total[col][raw - 1] == "X":
                for b in range(9-col):
                    if total[col][raw - b] == "O":
                        for c in range(b+1):
                            total[col][raw - c] == "O"
                        break

        if total[col][raw - 1] == "O":
            if total[col][raw + 1] == "O":
                total[col][raw] == "O"
            elif total[col][raw + 1] == "X":
                for b in range(9-col):
                    if total[col][raw + b] == "O":
                        for c in range(b+1):
                            total[col][raw + c] == "O"
                        break

        if total[col - 1][raw + 1] == "O":
            if total[col + 1][raw - 1] == "O":
                total[col][raw] == "O"
            elif total[col + 1][raw - 1] == "X":
                for b in range(9-col):
                    if total[col + b][raw - b] == "O":
                        for c in range(b+1):
                            total[col + c][raw - c] == "O"
                        break

        elif total[col - 1][raw - 1]  == "O":
            if total[col + 1][raw + 1] == "O":
                total[col][raw] == "O"
            elif total[col + 1][raw + 1] == "X":
                for b in range(9 - col):
                    if total[col + b][raw + b] == "O":
                        for c in range(b+1):
                            total[col + c][raw - c] == "O"
                        break

        elif total[col + 1][raw + 1] == "O":
            if total[col - 1][raw - 1] == "O":
                total[col][raw] == "O"
            elif total[col - 1][raw - 1] == "X":
                for b in range(9 - col):
                    if total[col - b][raw - b] == "O":
                        for c in range(b+1):
                            total[col + c][raw - c] == "O"
                        break

        elif total[col + 1][raw - 1] == "0":
            if total[col - 1][raw + 1] == "O":
                total[col][raw] == "O"
            elif total[col - 1][raw + 1] == "X":
                for b in range(9 - col):
                    if total[col - b][raw + b] == "O":
                        for c in range(b+1):
                            total[col + c][raw - c] == "O"
                        break

    elif total[col][raw] == "O":
        if total[col - 1][raw] == "X":
            if total[col + 1][raw] == "X":
                total[col][raw] == "X"
            elif total[col + 1][raw] == "O":
                for b in range(9-col):
                    if total[col + b][raw] == "X":
                        for c in range(b+1):
                            total[col + c][raw] == "X"
                        break

        if total[col + 1][raw] == "X":
            if total[col - 1][raw] == "X":
                total[col][raw] == "X"
            elif total[col - 1][raw] == "O":
                for b in range(9-col):
                    if total[col - b][raw] == "X":
                        for c in range(b+1):
                            total[col - c][raw] == "X"
                        break

        if total[col][raw + 1] == "X":
            if total[col][raw - 1] == "X":
                total[col][raw] == "X"
            elif total[col][raw - 1] == "O":
                for b in range(9-col):
                    if total[col][raw - b] == "X":
                        for c in range(b+1):
                            total[col][raw - c] == "X"
                        break

        if total[col][raw - 1] == "X":
            if total[col][raw + 1] == "X":
                total[col][raw] == "X"
            elif total[col][raw + 1] == "O":
                for b in range(9-col):
                    if total[col][raw + b] == "X":
                        for c in range(b+1):
                            total[col][raw + c] == "X"
                        break

        if total[col - 1][raw + 1] == "X":
            if total[col + 1][raw - 1] == "X":
                total[col][raw] == "X"
            elif total[col + 1][raw - 1] == "O":
                for b in range(9 - col):
                    if total[col + b][raw - b] == "X":
                        for c in range(b+1):
                            total[col + c][raw - c] == "X"
                        break

        elif total[col - 1][raw - 1] == "X":
            if total[col + 1][raw + 1] == "X":
                total[col][raw] == "X"
            elif total[col + 1][raw + 1] == "O":
                for b in range(9 - col):
                    if total[col + b][raw + b] == "X":
                        for c in range(b+1):
                            total[col + c][raw - c] == "X"
                        break

        elif total[col + 1][raw + 1] == "X":
            if total[col - 1][raw - 1] == "X":
                total[col][raw] == "X"
            elif total[col - 1][raw - 1] == "O":
                for b in range(9 - col):
                    if total[col - b][raw - b] == "X":
                        for c in range(b+1):
                            total[col + c][raw - c] == "X"
                        break

        elif total[col + 1][raw - 1] == "X":
            if total[col - 1][raw + 1] == "X":
                total[col][raw] == "X"
            elif total[col - 1][raw + 1] == "O":
                for b in range(9 - col):
                    if total[col - b][raw + b] == "X":
                        for c in range(b+1):
                            total[col + c][raw - c] == "X"
                        break

for i in range(int(input())):
    num = int(input())
    total = list(["+"]*8 for k in range(8))
    total[3][3] = "O"
    total[4][4] = "O"
    total[3][4] = "X"
    total[4][3] = "X"
    cnt = 0
    for j in range(num):
        col, raw = list(map(int, input().split()))
        col -= 1
        raw -= 1
        if cnt % 2 == 0:
            total[col][raw] = "X"
            foo(total, col, raw)
        else:
            total[col][raw] = "O"
            foo(total, col, raw)
        cnt += 1

    bk = 0
    wt = 0
    for n in total:
        for m in range(len(total)):
            if n[m] == "O":
                wt += 1
            elif n[m] == "X":
                bk += 1
    print(bk, wt)
    for k in total:
        print(k)