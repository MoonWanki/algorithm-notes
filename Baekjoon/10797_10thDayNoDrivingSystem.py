# BACKJOON #10797 <10부제>
# https://www.acmicpc.net/problem/10797

n = int(input())
c = 0
for v in list(input().split(' ')):
    if n == int(v): c = c+1
print(c)