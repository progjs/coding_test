# https://www.acmicpc.net/problem/4344
# 평균은 넘겠지

c = int(input())
ans = []

for i in range(c):
    scores = list(map(int, input().split()))
    n, scores = scores[0], scores[1:]
    avg = sum(scores)/n
    cnt = sum(list(map(lambda x: x>avg, scores)))
    ans.append(cnt/n * 100)

for a in ans: print(f'{a:.3f}%')    