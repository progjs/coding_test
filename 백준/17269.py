# 17269 이름궁합 테스트
# <https://www.acmicpc.net/problem/17269>

alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
alpha_dict = dict(zip(alph, num))
print(zip(alph, num))

n,m = map(int, input().split())
name1, name2 = input().split()
full_names = []
for i in range(n if n<m else m):
    full_names += [alpha_dict[name1[i]], alpha_dict[name2[i]]]
if n < m: # 남은 이름 뒤에 이어붙이기
    full_names += [alpha_dict[a] for a in name2[n:]]
else:
    full_names += [alpha_dict[a] for a in name1[m:]]

for _ in range(n+m-2): # 이름 알파벳 개수 -2 번 반복
    full_names = [(full_names[i]+full_names[i+1]) % 10 for i in range(len(full_names)-1)]

if not full_names[0]: # 십의자리숫자 == 0
    print('{}%'.format(full_names[1]))
else:
    print('{}{}%'.format(full_names[0],full_names[1]))