# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별 : O(1)

def solution(n):
    x = n**0.5
    return int(x+1)**2 if n**0.5 % 1 == 0 else -1