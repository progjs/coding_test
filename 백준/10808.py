word = input()
alpha = [0]*26
a = ord('a')

for w in word:
    alpha[ord(w)-a] += 1

print(" ".join(str(n) for n in alpha))
# join 으로 출력하기
# 아스키코드 활용하기
