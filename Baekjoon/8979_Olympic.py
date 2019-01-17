# BACKJOON #8979 <올림픽>
# https://www.acmicpc.net/problem/8979

import functools
N,K=map(int,input().split(' '))
a=sorted([list(map(int, input().split(' '))) for _ in' '*N], key=functools.cmp_to_key(lambda x,y: y[1]-x[1] if x[1]!=y[1] else y[2]-x[2] if x[2]!=y[2] else y[3]-x[3] if x[3]!=y[3] else 1))
b,c=list(range(N+1)),1
for i in range(1,N):
    if a[i-1][1:]==a[i][1:]: b[i+1]=b[i]
for i in range(N):
    if a[i][0]==K: print(b[i+1])