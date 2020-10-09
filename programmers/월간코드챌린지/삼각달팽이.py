def solution(n):
    dr, dc = [1,0,-1], [0,1,-1]
    arr = [[0]*i for i in range(1, n+1)]
    dir, num = 0, 1
    r,c = 0, 0
    
    for size in range(n, 0, -1):
        arr[r][c] = num
        num += 1
        for _ in range(size-1):
            r += dr[dir]
            c += dc[dir]
            arr[r][c] = num
            num += 1

        dir = (dir + 1) % 3
        r += dr[dir]
        c += dc[dir]
        
    answer = []
    for a in arr:
        answer += a
    return answer