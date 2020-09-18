# https://www.acmicpc.net/problem/14890
# 경사로
from sys import stdin
input = stdin.readline

def test(N, L, lst):
    i, cur = 0, [0]*N
    for i in range(N-1):
        if lst[i] == lst[i+1]:
            continue
        # 높이 차이 1일때
        elif lst[i]-1 == lst[i+1]: # 높은칸->낮은칸
            if i+1+L > N:
                return False
            after = lst[i+1]
            for j in range(i+2, i+1+L):
                if lst[j] != after or cur[j]:
                    return False
            for a in range(i+1, i+1+L):
                cur[a] = 1
        elif lst[i]+1 == lst[i+1]: # 낮은칸->높은칸
            if i-L+1 < 0:
                return False
            before = lst[i]
            for j in range(i, i-L, -1):
                if lst[j] != before or cur[j]:
                    return False
            for a in range(i-L+1, i+1):
                cur[a] = 1
        else:
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