# https://www.acmicpc.net/problem/5052
# 전화번호 목록

from sys import stdin, stdout

def solve(num_list):
    num_list.sort()
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1][:len(num_list[i])]:
            return 'NO'
    else:
        return 'YES'

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    numbers = []
    for _ in range(n):
        numbers.append(stdin.readline().rstrip())
    
    stdout.write(solve(numbers))