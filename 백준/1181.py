# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181

n = int(input())
words = set()
for _ in range(n):
    words.add(input())

answer = sorted(words, key = lambda x: (len(x), x))
for a in answer:
    print(a)

