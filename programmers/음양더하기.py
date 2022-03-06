# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution1(absolutes, signs):
    answer = 0
    for n,s in zip(absolutes, signs) :
        answer += (n if s else -1*n)
        answer += n*(2*s-1)
    return answer    

# lambda 함수 사용하기
def solution2(absolutes, signs):
    return sum(list(map(lambda x: x[0] if x[1] else -1*x[0], zip(absolutes, signs) )))

# signs[i] 가 True, False 인 것 활용
def solution3(absolutes, signs):
    return sum([n*(2*s-1) for  n,s in zip(absolutes, signs)])    

'''
True = 1 
False = 0 인 것으로 부호 나타내려고 방정식을 구했다.
    True = 1 -> 1
    False = 0 -> -1
    => 방정식 : y = 2x-1

실제 정수 = absolutes[i] * (2*signs[i] -1) 
'''    