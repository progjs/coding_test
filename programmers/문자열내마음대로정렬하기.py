# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))

'''
a를 정렬하는 방법

sorted(a)

- 2가지 기준으로 정렬
sorted(a, key = lambda x: (x[0], x[1]))

- 역순 정렬
sorted(a, key = lambda x: -x[0])
'''