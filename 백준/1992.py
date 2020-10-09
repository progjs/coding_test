# https://www.acmicpc.net/problem/1992
# 쿼드트리
answer = ''
delta = [(0,0), (0,1), (1,0), (1,1)]

def quard(row, col, size):
    global delta, answer
    
    if size == 1:
        answer += str(arr[row][col])
        return

    cur = arr[row][col]
    breakpoint = False
    for i in range(row, row+size):
        for j in range(col, col+size):
            if cur != arr[i][j]:
                answer += '('
                for d in delta:
                    quard(row+d[0]*size//2, col+d[1]*size//2, size//2)
                answer += ')'

                breakpoint = True
                break
        if breakpoint:
            break
    else:
        answer += str(cur)
        

if __name__ == "__main__":       
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]

    quard(0,0, n)
    print(answer)
