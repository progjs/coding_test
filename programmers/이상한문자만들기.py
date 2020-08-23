# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930#
# 공백이 "hello   world" 일때 주의!

def solution(s):
    answer = ''
    idx = 0
    for w in s:
        if w == ' ':
            answer += w
            idx = 0
        else:
            answer += w.upper() if idx % 2 == 0 else w.lower()
            idx += 1
    return answer