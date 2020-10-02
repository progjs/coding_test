# https://www.acmicpc.net/problem/15683
# 감시
'''
실패한 코드
원인: 감시카메라를 찾았을 때마다 사각지대를 최소로 하는 방향을 정하는데,
이후 다른 감시카메라 방향의 영향을 고려할 수 없다.

반례: 
4 6
2 6 0 3 0 2
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 6 1

답 = 8 
26#3#2 --> 3ㄱ 2ㅡ 1|
#00#0#
#00#0#
#00#61

틀린답 = 9
2603#2
#00#0#
#00#0#
#00#61
'''

N, M, board = 0, 0, []
dr, dc = (-1,1,0,0), (0,0,-1,1)
cam_dir = {'1':[[0], [1], [2], [3]], '2':[[0,1], [2,3]], '3':[[0,3], [1,3], [1,2], [0,2]], '4':[[0,1,2], [0,2,3], [1,2,3], [0,1,3]], '5':[[0,1,2,3]]}

def check(direction, cur_r, cur_c):
    global N, M, board, cam_dir

    for dir in cam_dir[board[cur_r][cur_c]][direction]:
        nr, nc = cur_r, cur_c
        while True:
            nr += dr[dir]
            nc += dc[dir]
            if 0<=nr<N and 0<=nc<M and board[nr][nc] != '6':
                if board[nr][nc] == '0':
                    board[nr][nc] = '#'
            else:
                break


# 방향이 주어지면, 감시할 수 있는 영역 개수 출력
def search(dir, cur_r, cur_c):
    global N, M, board

    cnt, nr, nc = 0, cur_r, cur_c
    while True:
        nr += dr[dir]
        nc += dc[dir]
        if 0<=nr<N and 0<=nc<M and board[nr][nc] != '6':
            # if board[nr][nc] == '0':
            cnt += 1
        else:
            break
    return cnt


# 카메라의 최대 감시영역 수 찾기
def search_max(r, c): 
    global cam_dir, board

    ans = [-1, -1] # 카메라 방향 case, 감시영역 수
    for idx, dirs in enumerate(cam_dir[board[r][c]]):
        cur_count = 0
        for d in dirs:
            cur_count += search(d, r, c)
        if ans[1] < cur_count:
            ans = [idx, cur_count]

    check(ans[0], r, c)


if __name__ == "__main__":
    N,M = map(int, input().split())
    board = [list(input().split()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != '#' and 0 < int(board[i][j]) < 6:
                search_max(i, j)
               
    answer = 0
    for i in range(N):
        answer += board[i].count('0')
    print(answer)                