# 청소년 상어

dr = (-1,-1,0,1,1,1,0,-1)
dc = (0,-1,-1,-1,0,1,1,1)




if __name__ == "__main__":
    arr = [list() for _ in range(4)]
    for i in range(4):
        a = list(map(int, input().split()))
        for j in range(0,8,2):
            arr[i].append([a[j], a[j+1]])
    for a in arr:
        print(a)

    