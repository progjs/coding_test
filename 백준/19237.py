dr = (-1,1,0,0)
dc = (0,0,-1,1) # 상하좌우

def update_smell():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]
            elif smell[i][j][1] == 1:
                smell[i][j] = [0, 0]
            elif smell[i][j][1] > 1:
                smell[i][j][1] -= 1
                    

def move():
    # 우선순위에 따라 상하좌우 탐색
    for idx, shark in sharks.items():
        r, c, d = shark
        for i in priority[idx][d-1]:
            nr, nc = r+dr[i-1], c+dc[i-1]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if smell[nr][nc][1] == 0: # 이동위치 발견
                arr[r][c] = 0
                sharks[idx] = [nr, nc, i]
                break
        if arr[r][c] == 0: # 냄새 없는곳 찾았으면
            continue
        # 냄새 없는곳 못찾았으면
        for i in priority[idx][d-1]: # 같은 상어의 냄새를 우선순위에 따라 탐색
            nr, nc = r+dr[i-1], c+dc[i-1]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if smell[nr][nc][0] == idx:
                arr[r][c] = 0
                sharks[idx] = [nr, nc, i]
                break
    
    deletes = []
    for idx, s in sharks.items(): # 상어 위치 이동
        r,c,d = s
        if arr[r][c] == 0:
            arr[r][c] = idx
        elif arr[r][c] < idx:
            deletes.append(idx)
        else:
            deletes.append(arr[r][c])
            arr[r][c] = idx

    for d in deletes: # 상어 제거
        del(sharks[d])


if __name__ == "__main__":
    N, M, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dirs = list(map(int, input().split())) # 상어 방향

    priority = {}
    for i in range(M):
        priority[i+1] = [list(map(int, input().split())) for _ in range(4)]

    sharks = {} # 상어=[row, col, 방향]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                sharks[arr[i][j]] = [i, j, dirs[arr[i][j]-1]]

    smell = [[[0,0]]*N for _ in range(N)] # [상어, 냄새]
    time = 0
    while time < 1000:
        update_smell()
        move()
        time += 1
        
        if len(sharks) == 1: # 1번 상어만 남았는지 체크
            print(time)
            break
    else:
        print(-1)