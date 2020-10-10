# RGB거리

N = int(input())
colors = []
for _ in range(N):
    colors.append(list(map(int, input().split())))

d = [[0]*3 for _ in range(N)]
d[0][0] = colors[0][0]
d[0][1] = colors[0][1]
d[0][2] = colors[0][2]
for i in range(N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + colors[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + colors[i][1]
    d[i][2] = min(d[i-1][1], d[i-1][0]) + colors[i][2]

print(min(min(d[N-1][0], d[N-1][1]), d[N-1][2]))