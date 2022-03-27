# 없는 숫자 더하기
def solution1(numbers):
    num_cnt = [0]*10
    
    for num in numbers:
        num_cnt[num] += 1
    
    answer = 0
    for i,c in enumerate(num_cnt):
        if c == 0:
            answer += i
    
    return answer

def solution2(numbers):
    return sum(range(0,10)) - sum(numbers)