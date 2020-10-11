# https://www.acmicpc.net/problem/15684
# 사다리 조작

from itertools import combinations

answer = 9876543210

def cal_power(teammem):
    p = 0
    for i in teammem:
        for j in teammem:
            p += s[i][j]
    return p


def min_power(t1, t2):
    global answer
    power = abs(cal_power(t1) - cal_power(t2))
    answer = min(power, answer)
    

if __name__=="__main__":
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    team = set(range(N))

    for case in combinations(list(range(N)), N//2):
        min_power(list(case), list(team - set(case)))

    print(answer)