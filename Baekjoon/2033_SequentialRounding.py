# BACKJOON #2033 <반올림>
# https://www.acmicpc.net/problem/2033

# 정수 N이 주어져 있을 때 이 수가 10보다 크면 일의 자리에서 반올림을 하고
# 이 결과가 100보다 크면 다시 10의 자리에서 반올림을 하고
# 또 이 수가 1000보다 크면 100의 자리에서 반올림을 하고... (이하 생략)
# 이러한 연산을 한 결과를 출력하시오.

import math
n=int(input())
if n:
    logged=int(math.log10(n))
    for i in range(logged):
        n=int(round(n+0.1,-i-1))
    print(n)
else: print(0)