# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


numbers = [6, 10, 2]
print(solution2(numbers))


'''
solution1() - fail 예외케이스
numbers = [200,20] => answer = 20020
numbers = [20,200] => answer = 20200

정답은 20200 이지만, 뒤에 0으로 채우면
200 -> 2000
20 -> 2000 으로 동일해서, 제대로 정렬되지않음.
'''
def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x.ljust(4,'0'), reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))
