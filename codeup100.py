# 1001
print('Hello')

# 1002
print('Hello World')

# 1003
print('Hello')
print('World')

# 1004
print("'Hello'")

# 1005
print('"Hello World"')

# 1006
print('"!@#$%^&*()"')

# 1007
print('"C:\Download\hello.cpp"')

# 1008
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print('\u250C\u252C\u2510')
print('\u251C\u253C\u2524')
print('\u2514\u2534\u2518')

# 1010
number = int(input())
print(number)

# 1011
data = input()
print(data)

# 1012
num = float(input())
print('%.6f' %num)

# 1013
a,b = input().split()
print(a+' '+b)

# 1014
a,b = input().split()
print(b+' '+a)

# 1015
num = float(input())
print('%.2f'%num)

# 1017
n = input()
print(n+' '+n+' '+n)

# 1018
time = input()
print(time)

# 1019
year, month, day = input().split('.')
print('{0}.{1}.{2}'.format(year.zfill(4), month.zfill(2), day.zfill(2)))

# 1020
d1, d2 = input().split('-')
print(d1+d2)

# 1021
word = input()
print(word)

# 1022
sentence = input()
print(sentence)

# 1023
n,f = input().split('.')
print(n)
print(f)

# 1024
word = input()
for w in list(word):
    # print(f"'{w}'")
    print("'{}'".format(w))

# 1025
num = input()
m = 10000
for n in list(num):
    print('[{}]'.format(int(n)*m))
    m = int(m/10)

# 1026
timelist = input().split(':')
print(int(timelist[1]))

# 1027
y, m, d = input().split('.')
print('{}-{}-{}'.format(d.zfill(2), m.zfill(2), y.zfill(4)))

# 1028 (unsigned int)
n = input()
print(n)

# 1029
n = float(input())
print('{:.11f}'.format(n))

# 1030 (long long int)
n = input()
print(n)

# 1031 (8진수 출력)
# 2진수로 bin(), 16진수로 hex()
n10 = int(input())
print(oct(n10)[2:])

# 1032
n = int(input())
print(hex(n)[2:])

# 1033
n = int(input())
print(hex(n)[2:].upper())

# 1034
o = input()
print(int('0o'+o, 8))

# 1035 (16진수->8진수)
# 16진수:0x 8진수:0o 2진수:0b
n16 = input()
print(oct(int('0x'+n16, 16))[2:])

# 1036 (문자->아스키코드)
# 아스키코드->문자 : chr(숫자)
a = input()
print(ord(a))

# 1037
n = int(input())
print(chr(n))

# 1038, 1039
n1, n2 = map(int, input().split())
print(n1+n2)

# 1040
n = int(input())
print(-n)

# 1041
a = input()
print(chr(ord(a)+1))

# 1042 (몫)
a, b = map(int, input().split())
print(a//b)

# 1043
a, b = map(int, input().split())
print(a%b)

# 1044
n = int(input())
print(n+1)

# 1045
a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('{:.2f}'.format(a/b))

# 1046
a,b,c = map(int, input().split())
total_sum = a+b+c
print(total_sum)
print('{:.1f}'.format(total_sum/3))

# 1047 (비트연산자)
'''
<<1 : 2배
<<2 : 4배
>>1 : 1/2배
'''
n = int(input())
print(n<<1)

# 1048 (a* 2^b)
a, b = map(int, input().split())
print(a<<b)

# 1049
a,b = map(int, input().split())
if a > b:
    print(1)
else:
    print(0)

# 1050
a,b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)

# 1051
a,b = map(int, input().split())
print(1 if a <= b else 0)

# 1052
a, b = input().split()
print(a and b)

# 1053
a = int(input())
print(int(not a))

# 1054
a,b = map(int, input().split())
print(a&b)

1055
a,b = map(int, input().split())
print(a or b)

# 1056 XOR
a,b = map(int, input().split())
print(a^b)

# 1057
a,b = map(int, input().split())
print(int(not(a^b)))

# 1058
a,b = map(int, input().split())
print(int(not a and not b))

# 1059
n = int(input())
print(~n)

# 1060
a,b = map(int, input().split())
print(a & b)

# 1061
a,b = map(int, input().split())
print(a | b)

# 1062
a,b = map(int, input().split())
print(a ^ b)

# 1063
a,b = map(int, input().split())
print(a) if a > b else print(b)

# 1064
a,b,c = map(int, input().split())
print(a if a<b else b) if (a if a<b else b) < c else print(c)

# 1065
numbers = list(map(int, input().split()))
for n in numbers:
    if n%2 == 0:
        print(n)

# 1066
nums = list(map(int, input().split()))
for n in nums:
    print('even') if n%2 == 0 else print('odd')

# 1067
n = int(input())
if n < 0:
    print('minus')
else:
    print('plus')

if n % 2 == 0:
    print('even')
else:
    print('odd')

# 1068
score = int(input())
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 40:
    print('C')
else:
    print('D')

# 1069
score = input()
if score == 'A':
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run!')
elif score == 'D':
    print('slowly~')
else:
    print('what?')

# 1070
month = int(input())
if 3 <= month <= 5:
    print('spring')
elif 6 <= month <= 8:
    print('summer')
elif 9 <= month <= 11:
    print('fall')
else:
    print('winter')

# 1071
lst = list(map(int, input().split()))
i = 0
while i < len(lst):
    if lst[i] == 0:
        break
    print(lst[i])
    i += 1

1072
cnt = int(input())
numbers = list(map(int, input().split()))
for n in numbers:
    print(n)

# 1073
numbers = list(map(int, input().split()))
for n in numbers:
    if n == 0:
        break
    print(n)

# 1074
cnt = int(input())
while cnt > 0:
    print(cnt)
    cnt -= 1

# 1075
cnt = int(input())
while cnt > 0:
    print(cnt-1)
    cnt -= 1

# 1076
a = ord(input())
cur = ord('a')
while cur <= a:
    print(chr(cur))
    cur += 1

# 1077
n = int(input())
for i in range(n+1):
    print(i)

# 1078
n = int(input())
total = 0
for even in range(2,n+1,2):
    total += even
print(total)

# 1079
data = list(input().split())
for a in data:
    print(a)
    if a == 'q':
        break
    
# 1080
end = int(input())
cur, total = 1, 0
while total < end:
    total += cur
    cur += 1
print(cur-1)

# 1081
n,m = map(int, input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

# 1082
x = input()
for t in range(1,16):
    print('{}*{}={}'.format(x,hex(t)[2:].upper(),hex(int(x,16)*t)[2:].upper()))

# 1083
end = int(input())
for n in range(1,end+1):
    if n % 3 == 0:
        print('X', end=' ')
    else:
        print(n, end=' ')

# 1084
r,g,b = map(int, input().split())
for rr in range(r):
    for gg in range(g):
        for bb in range(b):
            print(rr,gg,bb)
print(r*g*b)

# 1085
lst = list(map(int, input().split()))
t = 1
for n in lst:
    t *= n
print('{:.1f} MB'.format(t/8/1024/1024))

# 1086
w,h,b = map(int, input().split())
print('{:.2f} MB'.format(w*h*b/8/1024/1024))

# 1087
end = int(input())
total = 0
for n in range(1, end+1):
    total += n
    if total >= end:
        print(total)
        break

# 1088
end = int(input())
for n in range(1,end+1):
    if n % 3:
        print(n, end=' ')

# 1089 : 등차수열
a, d, n = map(int, input().split())
print(d*(n-1)+a)

# 1090 : 등비수열
a,r,n = map(int, input().split())
print(a*r**(n-1))

# 1091 : 곱하고 더하는 수열
a,m,d,n = map(int, input().split())
nxt = a
for _ in range(n-1):
    nxt = nxt*m + d
print(nxt)

1092
a,b,c = map(int, input().split())
ans = max(a,b,c)
while True:
    if (ans%a==0) and (ans%b==0) and (ans%c==0):
        print(ans)
        break
    ans += 1

def gcd(x,y):
    if y == 0:
        return y
    return gcd(y,x%y)

# 1093
n = int(input())
cnt_list = [0]*24
call = map(int, input().split())

for c in call:
    cnt_list[c] += 1

for i in cnt_list[1:]:
    print(i, end=' ')

# 1094
n = int(input())
lst = list(input().split())

for i in lst[::-1]:
    print(i, end=' ')

# 1095
cnt = input()
lst = list(map(int, input().split()))
first = lst[0]

for n in lst[1:]:
    if first > n:
        first = n

print(first)

# 1096
n = int(input())
arr = [[0]*19 for _ in range(19)]
for _ in range(n):
    x,y = map(int, input().split())
    arr[y-1][x-1] = 1

for i in range(19):
    for j in range(19):
        print(arr[j][i], end=' ')
    print()

#  1097
arr = []
for _ in range(19):
    lst = list(map(int, input().split()))
    arr.append(lst)

n = int(input())
for _ in range(n):
    x,y = map(int, input().split())

    for i in range(19): # 가로
        arr[x-1][i] = 1-arr[x-1][i]

    for i in range(19): # 세로
        arr[i][y-1] = 1-arr[i][y-1]

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()

# 1098
h, w = map(int, input().split())
n = int(input())
dir = [] # 막대길이, 방향(가로0, 세로1), x,y(가장 왼쪽,위쪽)
for _ in range(n):
    dir.append(list(map(int, input().split())))

arr = [[0]*w for _ in range(h)]

for d in dir:
    x,y = d[2], d[3]
    if d[1]:
        for i in range(d[0]):
            newX, newY = x-1+i, y-1
            if 0 <= newX < h and 0 <= newY < w:
                arr[newX][newY] = 1
    else:
        for i in range(d[0]):
            newX, newY = x-1, y-1+i
            if 0 <= newX < h and 0 <= newY < w:
                arr[newX][newY] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()

# 1099
arr = [list(map(int, input().split())) for _ in range(10)]
cur = [1,1]

while cur != [9,9]:
    if arr[cur[0]][cur[1]] == 2:
        break

    arr[cur[0]][cur[1]] = 9
    if (cur[1] != 8) and (arr[cur[0]][cur[1]+1] != 1):
        cur[1] += 1
    elif (cur[0] != 8) and (arr[cur[0]+1][cur[1]] != 1):
        cur[0] += 1
    else:
        break
arr[cur[0]][cur[1]] = 9

# print()
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()