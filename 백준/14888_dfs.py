# https://www.acmicpc.net/problem/14888
# 연산자 끼워 넣기


def cal(cur, cnt, add, minus, multi, div):
    global ans_min, ans_max, N, numbers

    if cnt == N:
        ans_max = cur if cur > ans_max else ans_max
        ans_min = cur if cur < ans_min else ans_min
        return

    if add > 0:
        cal(cur+numbers[cnt], cnt+1, add-1, minus, multi, div)

    if minus > 0:
        cal(cur-numbers[cnt], cnt+1, add, minus-1, multi, div)

    if multi > 0:
        cal(cur*numbers[cnt], cnt+1, add, minus, multi-1, div)

    if div > 0:
        cal(int(cur/numbers[cnt]), cnt+1, add, minus, multi, div-1)


if __name__ == '__main__':
    N = int(int(input()))
    numbers = list(map(int, input().split()))
    a, m, mt, d = map(int, input().split())
    #   +-*%

    ans_max, ans_min = -9876543210, 9876543210
    cal(numbers[0], 1, a, m, mt, d)
    print(ans_max)
    print(ans_min)
