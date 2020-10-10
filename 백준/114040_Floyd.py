# https://www.acmicpc.net/problem/11404
# 플로이드

from sys import maxsize, stdin, stdout

INF = maxsize
input = stdin.readline
print = stdout.write

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                arr[i][j]= min(arr[i][j], arr[i][k]+arr[k][j])


if __name__=="__main__":
    N = int(input()) # 도시
    M = int(input()) # 버스

    arr = [[INF]*N for _ in range(N)]
    for i in range(N):
        arr[i][i] = 0
        
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a-1][b-1] = min(c, arr[a-1][b-1])
    
    floyd()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == INF:
                print('0 ')
            else:
                print(str(arr[i][j])+' ')
        print('\n')

