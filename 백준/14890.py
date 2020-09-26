# https://www.acmicpc.net/problem/14890
# 경사로
'''
경사로를 놓을 수 있다면(높이 차이 = 1)
    낮은칸이 L개인지 & 경사로가 없는지 확인

- 높은칸(i)->낮은칸 일 때
    i+1 ~ i+L-1까지(L개) 확인
- 낮은칸(i)->높은칸 일 때
    i-L+1 ~ i까지(L개) 확인

경사로 설치가 가능하면
    경사로를 설치하는 위치를 저장(기억한다)
'''

from sys import stdin
input = stdin.readline

def test(N, L, lst):
    i, cur = 0, [0]*N

    for i in range(N-1):
        if lst[i] == lst[i+1]:
            continue

        # 높이 차이 1일때
        elif lst[i]-1 == lst[i+1]: # 높은칸->낮은칸
            if i+1+L > N: # index 초과
                return False
            after = lst[i+1]
            for j in range(i+2, i+1+L):
                if lst[j] != after or cur[j]: # 경사로가 있는지, 높이가 같은지
                    return False
            for a in range(i+1, i+1+L): # 경사로 설치하는 위치 기억
                cur[a] = 1

        elif lst[i]+1 == lst[i+1]: # 낮은칸->높은칸
            if i-L+1 < 0: # index 초과
                return False
            before = lst[i]
            for j in range(i, i-L, -1):
                if lst[j] != before or cur[j]: # 경사로가 있는지, 높이가 같은지
                    return False
            for a in range(i-L+1, i+1): # 경사로 설치하는 위치 기억
                cur[a] = 1

        else: # 높이가 2이상 차이날 때
            return False
    return True

if __name__ == "__main__":
    N, L = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = 0
    for r in board:
        answer += test(N, L, r)
    for i in range(N):
        answer += test(N, L, [board[a][i] for a in range(N)])
    print(answer)