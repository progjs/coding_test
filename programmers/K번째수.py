# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution1(array, commands):
    answer = []
    
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer

# lambda 함수 사용하기
def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

    