# https://www.acmicpc.net/problem/15683
# 감시
'''
1. 감시카메라 위치를 cctv에 저장
2. (dfs) 모든 감시카메라의 방향 정하기
3. 감시카메라의 방향을 모두 정했을 때, # 표시
4. 사각지대(0) 너비 세기(=result)
5. result < answer => answer 업데이트
6. 2~5번 반복
'''

import copy

answer = 100
cctv = [] # 모든 카메라의 방향을 담는다.
dr, dc = (-1,1,0,0), (0,0,-1,1)
cctv_dict = {'1':[[0], [1], [2], [3]], '2':[[0,1], [2,3]], '3':[[0,3], [1,3], [1,2], [0,2]], '4':[[0,1,2], [0,2,3], [1,2,3], [0,1,3]], '5':[[0,1,2,3]]}


# 방향이 주어지면, 감시할 수 있는 영역 #으로 표시
def check(dir, cur_r, cur_c, copy_board):
    global dr, dc
    cnt, nr, nc = 0, cur_r, cur_c
    while True:
        nr += dr[dir]
        nc += dc[dir]
        if 0<=nr<N and 0<=nc<M and copy_board[nr][nc] != '6':
            if copy_board[nr][nc] == '0':
                copy_board[nr][nc] = '#'
        else:
            return copy_board


def search_dfs(n, cctv_dir):
    global answer, board, cctv_dict

    if n == len(cctv): # 모든 감시카메라의 방향을 정했을 때
        copy_board = copy.deepcopy(board) # 복사

        for idx, dirs in enumerate(cctv_dir):
            cur_r, cur_c = cctv[idx][0], cctv[idx][1]
            for d in dirs:
                copy_board = check(d, cur_r, cur_c, copy_board)

        result = 0 # 감시 못하는 영역 count
        for c in range(N):
            result += copy_board[c].count('0')
        if answer > result:
            answer = result
        return
    
    # 감시카메라 방향 설정
    r, c = cctv[n][0], cctv[n][1]
    for idx, dir in enumerate(cctv_dict[board[r][c]]):
        cctv_dir.append(dir)
        search_dfs(n+1, cctv_dir)
        cctv_dir.pop()


if __name__ == "__main__":
    N,M = map(int, input().split())
    board = [list(input().split()) for _ in range(N)]

    for i in range(N): # 감시카메라 찾기
        for j in range(M):
            if board[i][j] != '#' and 0 < int(board[i][j]) < 6:
                cctv.append([i, j])
    
    search_dfs(0, []) # cctv 방향: [i,j,방향]
    print(answer)                