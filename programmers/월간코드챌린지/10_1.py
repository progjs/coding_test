def solution(n):
    answer = ''
    while n >= 3:
        answer += str(n%3)
        n = n//3
    answer += str(n)
    result, t = 0, 1
    for a in answer[::-1]:
        result += t*int(a)
        t *= 3
    return result

print(solution(45)) # 7
print(solution(125)) # 229

'''
n	result
45	7
125	229
'''