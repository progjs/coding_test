data = [4,5,6]
ans = [[1,2,9,3,10,8,4,5,6,7], [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9], [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]]

def solution(n):
    answer = []
    arr = [[0]*i for i in range(1, n+1)]
    dir = 0
    num = 1
    turns = [0, n-1, -1]
    for size in range(n, 0, -1):
        dir %= 3
        if dir == 0:
            start = (n-size)//2 +1
            for i in range(start, start+size):
                arr[i][turns[0]] = num
                num += 1
            turns[0] += 1
        
        elif dir == 1:
            start = n-turns[1]
            for i in range(start, start+size):
                arr[turns[1]][i] = num
                num += 1
            turns[1] -= 1

        else:
            start = n-size-1
            for i in range(start, start-size,-1):
                arr[i][turns[2]] = num
            turns[2] -= 1

        dir += 1

    return arr

for i in range(3):
    print(ans[i])
    print(solution(data[i]))
    
