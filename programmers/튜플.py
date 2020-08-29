# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    lst = list(s[2:-2].split('},{'))
    Sorted = sorted([tuple(map(int, l.split(','))) for l in lst], key = lambda x: len(x))

    answer = [Sorted[0][0]]
    for i in range(len(Sorted)-1):
        answer += list(set(Sorted[i+1]) - set(Sorted[i])) # 차집합
    return answer