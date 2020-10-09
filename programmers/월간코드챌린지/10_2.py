'''
입출력 예
arr	result
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	[4,9]
[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]	[10,15]
'''

# arr, answer = [], [0,0]
# delta = [(0,0), (1,0), (0,1), (1,1)]

# def quard(row, col, size):
#     global answer, delta, arr
#     if size == 1:
#         for d in delta:
#             answer[arr[row+d[0]][col+d[1]]] += 1
#         return
    
#     for d in delta:
#         start_r = row+d[0]*size
#         start_c = col+d[1]*size
#         cur = arr[start_r][start_c]
#         breakpoint = False
        
#         for i in range(start_r, start_r+size):
#             for j in range(start_c, start_c+size):
#                 if cur != arr[i][j]:
#                     quard(start_r, start_c, size//2)
#                     breakpoint = True
#                     break
#             if breakpoint:
#                 break
#         else:
#             answer[cur] += 1

# def solution(arr2):
#     global answer, arr
#     arr = [aa for aa in arr2]
#     n = len(arr)
    
#     cur = arr[0][0]
#     breakpoint = False
#     for i in range(n):
#         for j in range(n):
#             if cur != arr[i][j]:
#                 quard(0,0, n//2)
#                 breakpoint = True
#                 break
#         if breakpoint:
#             break
#     else:
#         answer[cur] = 1

#     return answer

# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# # 답 [4,9]
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# # 답 [10, 15]

arr, answer = [], []
delta = [(0,0), (1,0), (0,1), (1,1)]

def quard2(row, col, size):
    global answer, delta, arr
    
    if size == 1:
        answer[arr[row][col]] += 1
        return

    cur = arr[row][col]
    breakpoint = False
    for i in range(row, row+size):
        for j in range(col, col+size):
            if cur != arr[i][j]:
                breakpoint = True
                for d in delta:
                    quard2(row+d[0]*size//2, col+d[1]*size//2, size//2)
                break
        if breakpoint:
            break
    else:
        answer[cur] += 1
        
        
def solution2(arr2):
    global answer, arr
    arr = [aa for aa in arr2]
    n = len(arr)
    answer = [0, 0]
    
    quard2(0,0, n)
    return answer

print(solution2([[1,0], [1,1]]))
print(solution2([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# 답 [4,9]
print(solution2([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# 답 [10, 15]
