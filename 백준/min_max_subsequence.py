# 아직 푸는중

N = int(input())
numbers = list(map(int, input().split()))
d = [N] * N
d[0] = 1
if d[0]==d[1]:
    d[1] = 1
    start_idx = 1
else:
    d[1] = 2
    start_idx = 0

for idx, n in enumerate(numbers[2:]):
    start_n, end_n = numbers[start_idx], numbers[start_idx+d[idx-1]]
    if n < start_n and n < end_n: # new min
        pass
    elif n > start_n and n > end_n: # new max
        pass
    elif n == start_n:
        if d[idx-1] < abs(idx-start_n)+1:
            d[idx] = d[idx-1]

    elif n == end_n:
        pass
    else:
        d[idx] = d[idx-1]
print(d[N-1])