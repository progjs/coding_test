# https://programmers.co.kr/learn/courses/30/lessons/43162

'''
이 문제는 재귀를 사용하지만 bfs를 사용한 것이다.
check함수에서 for문으로 cur node에 인접한 모든 node를 방문해야하기 때문에
cur node에 인접하고 방문하지 않은 node를 하나 발견했다고 해서, 
바로 return이나 break로 for문을 벗어나면 안된다!
'''

def check(cur, visited, computers):
    visited[cur] = True
    for idx, value in enumerate(visited):
        if not value and computers[cur][idx]:
            check(idx, visited, computers)
            # break나 return으로 종료하면 안된다!
    

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            check(i, visited, computers)
            answer += 1
    return answer