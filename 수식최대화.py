from itertools import permutations
    
def solution(expression):
    numbers, operations = [], []
    num =''
    for e in expression:
        if e.isdigit():
            num += e
        else:
            numbers.append(int(num))
            num = ''
            operations.append(e)
    numbers.append(int(num))
    
    max_ans = 0 # 답
    for ops in permutations(['-', '*', '+']):
        operations_copy = operations[:]
        result = numbers[:]
        for cur_op in ops:
            while operations_copy and cur_op in operations_copy:
                idx = operations_copy.index(cur_op)
                operations_copy.pop(idx)
                if cur_op == '*':
                    result[idx] *= result.pop(idx+1)
                elif cur_op == '+':
                    result[idx] += result.pop(idx+1)
                elif cur_op == '-':
                    result[idx] -= result.pop(idx+1)
    
        if max_ans < abs(result[0]):
            max_ans = abs(result[0])
    return max_ans
    
