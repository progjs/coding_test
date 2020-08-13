# 괄호 변환
# <https://programmers.co.kr/learn/courses/30/lessons/60058>

def chk_balance(data):
    cnt = 0
    for idx, item in enumerate(data):
        cnt = cnt+1 if item=='(' else cnt-1
        if cnt == 0:
            return data[:idx+1], data[idx+1:]

def chk_right(data):
    stack = []
    for d in data:
        if d == '(':
            stack.append(d)
        elif not stack:
            return False
        else:
            stack.pop()
    return True
        
def solution(p):
    if not p:
        return ''

    u, v = chk_balance(p)
    if chk_right(u):
        return u + solution(v)
    else:
        chg = lambda x: ')' if x=='(' else '('
        return '('+ solution(v) + ')' + ''.join(list(map(chg, u[1:-1])))