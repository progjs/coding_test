# https://programmers.co.kr/learn/courses/30/lessons/43165

def cal(numbers, target):
    if not numbers:
        if target == 0:
            return True
        else:
            return False
    return cal(numbers[1:], target-numbers[0]) + cal(numbers[1:], target+numbers[0])

def solution(numbers, target):
    return cal(numbers, target)