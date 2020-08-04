# 프로그래머스 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(data):
    answer = len(data)
    for r in range(1,len(data)//2 +1):
        result, cnt, rep = '', 1, data[:r]
        for i in range(r, len(data), r):
            if data[i:i+r] == rep:
                cnt += 1
            else:
                result = result + rep if cnt == 1 else result + str(cnt) + rep
                cnt, rep = 1, data[i:i+r]
        result = result + rep if cnt == 1 else result + str(cnt) + rep
        if answer > len(result):
            answer = len(result)
    return answer
    