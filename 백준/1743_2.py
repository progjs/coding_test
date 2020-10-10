from collections import deque

dr, dc = [0,0,-1,1], [1,-1,0,0]

def bfs(row,col):
    queue = deque()
    arr[row][col] = 0
    queue.append([row,col])
    cnt = 1

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=M or not arr[nr][nc]:
                continue
            cnt += 1
            arr[nr][nc] = 0
            queue.append([nr, nc])
    return cnt

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        r,c = map(int, input().split())
        arr[r-1][c-1] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                answer = max(bfs(i, j), answer)

    print(answer)