# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

from collections import deque

sentence = ""
while True:
    sentence = input()
    if sentence == ".": break

    stack = deque()
    for w in sentence:
        if w in "([":
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                print("no")
                break
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break
   
    else:
        print("yes") if not stack else print("no")


