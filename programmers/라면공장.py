# 라면공장
# https://programmers.co.kr/learn/courses/30/lessons/42629

def solution(stock, dates, supplies, k):
    import heapq
    from collections import deque
    
    answer = 0
    heap = []
    dates = deque(dates + [k])
    supplies = deque(supplies)
    i = 0
    while i < k:
        if i == dates[0]:
            dates.popleft()
            heapq.heappush(heap, -supplies.popleft())
        if stock == 0:
            stock = -heapq.heappop(heap)
            answer += 1
        if i + stock <= dates[0]:
            i += stock
            stock = 0
        else:
            stock = stock-dates[0]+i
            i = dates[0]
    return answer