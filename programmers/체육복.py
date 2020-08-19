# <https://programmers.co.kr/learn/courses/30/lessons/42862>
# 체육복

def solution(n, lost, reserve):
    rv_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for rv in rv_set:
        if rv-1 in lost_set:
            lost_set.remove(rv-1)
        elif rv+1 in lost_set:
            lost_set.remove(rv+1)
    return n - len(lost_set)