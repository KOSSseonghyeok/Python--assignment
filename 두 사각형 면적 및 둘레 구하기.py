num = int(input())
length = 0
S = 0
for i in range(num):
    x1, y1, x2, y2 = list(map(int, input().split()))
    X1, Y1, X2, Y2 = list(map(int, input().split()))
    lix = [x1, x2, X1, X2]
    liy = [y1, y2, Y1, Y2]
    lix.sort()
    liy.sort()

    if (x2 < X1) or (X2 < x1) or (Y1 > y2) or (y1 > Y2): #안겹치는 거
        S = ((x2-x1)*(y2-y1)) + ((X2-X1)*(Y2-Y1))
        length = ((X2-X1)+(x2-x1)+(y2-y1)+(Y2-Y1))*2
    else:
        length = ((lix[3]-lix[0])+(liy[3]-liy[0]))*2
        S = ((x2-x1)*(y2-y1)) + ((X2-X1)*(Y2-Y1)) - (lix[2]-lix[1])*(liy[2]-liy[1])
    print(S, length)
