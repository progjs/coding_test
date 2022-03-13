# https://baaaaaaaaaaaaaaaaaaaaaaarkingdog.tistory.com/922?category=773649
'''
func1()
N 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을 반환하시오.
N: 50000 이하 자연수
'''
def check(x, cnt):
    return x*cnt*(cnt+1)

def func1(n): # 시간복잡도 O(n)
    return int( (check(3,n//3) + check(5,n//5) - check(15,n//15)) /2)

def test1():
    n = int(input())
    print(func1(n))


'''
func2(int list, int N)
주어진 길이 N의 정수배열 arr에서 합이 100인 서로다른 위치의 두 원소가 존재하면 1을,
존재하지 않으면 0을 반환하는 함수
list의 각 수는 [0,100] 
N: 1000 이하
'''
def func2(n, arr):  # O(n**2)
    for i in range(n):
        for j in arr[i+1:]:
            if arr[i]+j == 100: return 1
    return 0

def test2():    
    n = int(input())
    arr = list(map(int, input().split()))
    print(func2(3, arr))


'''
func4(N)
N 이하의 수 중에서 가장 큰 2의 거듭제곱수를 반환하는 함수
N: 10억 이하의 자연수
'''
def func4(n):   # O(logN)
    chk = 1
    while chk <= n:
        chk *= 2
    return chk // 2


def test4():
    d = [5, 97615282, 1024]
    for n in d:
        print(func4(n))    

