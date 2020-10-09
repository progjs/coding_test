'''
입출력 예
s	result
"baby"	9
"oo"	0
'''

# 실패
def solution(s):
    answer = 0
    chk, t = True, s[0]
    for x in s:
        if t != x:
            chk = False
            break
    else:
        return answer
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            start, end = i, j
            ans1, ans2 = 0,0
            while start < end:
                if s[start] != s[end]:
                    ans1 = end-start
                    break
                end -= 1

            start, end = i, j
            while start < end:
                if s[start] != s[end]:
                    ans2 = end-start
                    break
                start += 1
            answer += ans1 if ans1 > ans2 else ans2
    return answer

print(solution("baby"))
print(solution("ooooo"))
# print(solution("oboooo"))