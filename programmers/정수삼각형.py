# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수삼각형

def solution(triangle):
    for row in range(1, len(triangle)):
        for i in range(row+1):
            if i == 0:
                triangle[row][0] += triangle[row-1][0]
            elif i == row:
                triangle[row][-1] += triangle[row-1][-1]
            else:
                triangle[row][i] += max(triangle[row-1][i-1], triangle[row-1][i])
        
    return max(triangle[-1])