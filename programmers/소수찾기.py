# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    sleve = [True] * (n+1)    
    for number in range(2, int(n**0.5)+1):
        if sleve[number]:
            for b in range(number*2, n+1, number):
                sleve[b] = False

    answer = sum(sleve[2:])
    return answer