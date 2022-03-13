# https://www.acmicpc.net/problem/1912
# 연속합

from sys import stdin
input =  stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# dp 풀이법     O(n)
d = [0]*n
answer = d[0] = arr[0]

for i in range(1,n):
    d[i] = max(d[i-1] + arr[i], arr[i])
    answer = max(d[i], answer)

print(answer)    

'''
DP : 다이나믹 프로그래밍
중간결과를 저장 -> 속도가 빠름 
dp[i]를 나타내는 점화식을 찾는것이 중요!

1. dp[0] 초기값을 정하고
2. dp[i]를 정의
3. 답을 dp[-1]로 찾거나, dp를 채우면서 답을 찾아내기 -> for문
'''

# 시간초과
# O(n**2)~O(n**3) 시간복잡도라서 시간초과....
'''
answer = -10000000

for cnt in range(1,n+1):
    for i in range(n-cnt+1):
        s = sum(arr[i:i+cnt])
        answer = max(answer, s)

print(answer)
'''

