# https://www.acmicpc.net/problem/14888
# 연산자 끼워 넣기

from itertools import permutations

N = int(int(input()))
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))
opmap = []
for i,p in enumerate(opers):
    opmap += [i]*p
#   +-*%

ans_max, ans_min = -9876543210, 9876543210

for case in permutations(opmap, len(opmap)):
    ans = numbers[0]
    for i, b in enumerate(numbers[1:]):
        if case[i] == 0:
            ans += b
        elif case[i] == 1:
            ans -= b
        elif case[i] == 2:
            ans *= b
        else:
            ans = -(-ans//b) if ans < 0 else ans//b
    ans_max = ans if ans > ans_max else ans_max        
    ans_min = ans if ans < ans_min else ans_min

print(ans_max)
print(ans_min)
