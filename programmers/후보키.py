# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    col_len = len(relation[0])
    answer = []
    # 유일성검사
    for i in range(1,col_len+1):
        for com in combinations(range(col_len), i):
            keys = [tuple(r[idx] for idx in com) for r in relation]
            if len(set(keys)) == len(relation):
                answer.append(set(com))
    #최소성검사
    for a1 in answer[:]:
        for a2 in answer[:]:
            if a1 == a2: continue
            if a1 == a2 & a1: #교집합
                answer.remove(a2) 
    return len(answer)