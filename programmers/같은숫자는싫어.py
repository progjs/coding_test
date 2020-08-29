# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 슬라이싱 활용
def solution(arr):
    answer = []
    for a in arr:
        # 슬라이싱은 []빈 list를 index로 참조해도 에러가 나지 않는다
        if answer[-1:] != [a]: 
            answer.append(a)
    return answer

lst = list(range(1,10))
for a in lst[::]:
    a += 1
print(lst)
