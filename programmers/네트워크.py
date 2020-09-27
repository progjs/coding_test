# https://programmers.co.kr/learn/courses/30/lessons/43162

def dfs(root, visited, computers, cnt):
    visited[root] = True
    for i in range(len(visited)):
        if computers[root][i] and not visited[i]:
            computers[root][i], computers[i][root] = 0, 0
            return dfs(i, visited, computers, cnt+1)
    return cnt

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            print(dfs(i, visited, computers,1))
            answer += 1
    return answer