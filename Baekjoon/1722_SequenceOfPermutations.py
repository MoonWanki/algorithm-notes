# BACKJOON #1722 <순열의 순서>
# https://www.acmicpc.net/problem/1722

# 첫째 줄에 N(1≤N≤20)이 주어진다.
# 둘째 줄의 첫 번째 수는 소문제 번호이다.
# 1인 경우 k(1≤k≤N!)를 입력받고, 2인 경우 임의의 순열을 나타내는 N개의 수를 입력받는다.
# N개의 수에는 1부터 N까지의 정수가 한 번씩만 나타난다.
# k번째 수열을 나타내는 N개의 수를 출력하거나, 몇 번째 수열인지를 출력하면 된다.

import math
n=int(input())
fac=math.factorial(n)
k,*a=map(int, input().split())
l=list(range(1,n+1))
if k==1:
    a=a[0]-1
    while n>1:
        print(l[a//(fac//n)],end=' ')
        del l[a//(fac//n)]
        fac=fac//n
        n-=1
        a=a%fac
    print(l[0])
else:
    pos=0
    for e in a[:-1]:
        idx=l.index(e)
        pos+=(fac//n)*idx
        del l[idx]
        fac=fac//n
        n-=1
    print(pos+1)