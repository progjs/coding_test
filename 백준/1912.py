# https://www.acmicpc.net/problem/1912
# 연속합

from sys import stdin
input =  stdin.readline

n = int(input())
arr = list(map(int,input().split()))

d = [0]*n
answer = d[0] = arr[0]

for i in range(1,n):
    d[i] = max(d[i-1] + arr[i], arr[i])
    answer = max(d[i], answer)

print(answer)    


# 시간초과
# n^2~n^3 시간복잡도라서 시간초과....
'''
answer = -10000000

for cnt in range(1,n+1):
    for i in range(n-cnt+1):
        s = sum(arr[i:i+cnt])
        answer = max(answer, s)

print(answer)
'''

