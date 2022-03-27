from sys import stdin
from collections import deque

input = stdin.readline
left = deque(input().strip()) # 개행문자 제거
m = int(input())
right = deque()

for i in range(m):
    command = list(input().split())

    if command[0] == 'L' and left:   # 커서 왼쪽 이동
        right.append(left.pop())
    elif command[0] == 'D' and right: # 커서 오른쪽 이동
        left.append(right.pop())
    elif command[0] == 'B' and left: # 커서 왼쪽문자 삭제
        left.pop()
    elif command[0] == 'P':     # 커서 왼쪽에 문자 추가
        left.append(command[1])

right.reverse() # deque.reverse() 는 return type: None이라, print(deque.reverse()) 로 사용불가
print("".join( list(left) + list(right) ))

'''
시간초과 풀이 : python자체가 연산이 느리기때문인 것 같다..
그래서 cursor기준으로 left/right deque를 나누는 방식으로 구현함.

input = stdin.readline
data = input().strip() # 개행문자 제거
m = int(input())
cur = len(data)

for i in range(m):
    command = list(input().split())
    if command[0] == 'L':   # 커서 왼쪽 이동
        cur = max(0, cur-1)
    elif command[0] == 'D': # 커서 오른쪽 이동
        cur = min(len(data), cur+1)
    elif command[0] == 'B' and cur > 0: # 커서 왼쪽문자 삭제
        data = data[:cur-1] + data[cur:]
        cur = max(0, cur-1)
    elif command[0] == 'P':     # 커서 왼쪽에 문자 추가
        data = data[:cur] + command[1] + data[cur:]
        cur = min(len(data), cur+1)
    # print(str(i+1) + "번째 :" + data + " cur="+str(cur))
'''


