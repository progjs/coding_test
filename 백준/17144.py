def air_position():
    for i in range(R):
        if arr[i][0] == -1:
            return [i, 0], [i + 1, 0]  

def dust_move():
    temp = [[0] * C for _ in range(R)] 
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                val = 0 
                if i - 1 >= 0 and arr[i - 1][j] != -1: # 상
                    temp[i - 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5
                if i + 1 < R and arr[i + 1][j] != -1: # 하
                    temp[i + 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5
                if j - 1 >= 0 and arr[i][j - 1] != -1: # 좌
                    temp[i][j - 1] += arr[i][j] // 5
                    val += arr[i][j] // 5
                if j + 1 < C and arr[i][j + 1] != -1: # 우
                    temp[i][j + 1] += arr[i][j] // 5
                    val += arr[i][j] // 5
                temp[i][j] -= val 
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]  

def air_move():
    # 위로 - 1 아래쪽
    temp = arr[up[0]][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    arr[up[0]][1] = 0

    # 2 오른쪽
    temp_1 = arr[0][C - 1]
    for i in range(up[0] - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up[0] - 1][C - 1] = temp

    # 3 위쪽
    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    # 4 왼쪽
    for i in range(up[0] - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    # 아래로 - 1 위쪽
    temp = arr[down[0]][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down[0]][i] = arr[down[0]][i - 1]
    arr[down[0]][1] = 0

    # 2 오른쪽
    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down[0] + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down[0] + 1][C - 1] = temp

    # 3 아래쪽
    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    # 4 왼쪽
    for i in range(down[0] + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2

if __name__ == "__main__":
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    up, down = air_position()
    for i in range(T):
        dust_move()  
        air_move()  

    total = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                total += arr[i][j]
    print(total)