# https://www.acmicpc.net/problem/14501
# 퇴사

N = int(input())
tp = [list(map(int, input().split())) for _ in range(N)]
d = [0]*25

for i in range(N):
    # i날 일을 안하면 d[i+1] 에도 d[i]가 유지되니까 max(d[i+1], d[i])로 갱신
    d[i+1] = max(d[i], d[i+1])
    # i날 일을 하면 d[i+t[i]]를 갱신
    d[i+tp[i][0]] = max(d[i+tp[i][0]], d[i]+tp[i][1])

print(d[N])