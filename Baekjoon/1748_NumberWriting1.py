# BACKJOON #1748 <수 이어 쓰기 1>
# https://www.acmicpc.net/problem/1748
import math
n = int(input())
if n<10: print(n)
else:
    lg = int(math.log10(n))+1
    sum = 0
    nine = 9
    for i in range(1, lg):
        sum += nine * i
        nine *= 10
    sum += (n-10**(lg-1)+1)*lg
    print(sum)