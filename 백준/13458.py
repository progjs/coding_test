# 시험 감독
# https://www.acmicpc.net/problem/13458

from sys import stdin
input = stdin.readline

N = int(input())
students = list(map(int, input().split()))
b,c = map(int, input().split())

answer = N
for s in students:
    if s-b > 0:
        if (s-b) % c:
            answer += (s-b)//c +1
        else:
            answer += (s-b)//c
print(answer)