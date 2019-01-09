# BACKJOON #2193 <이친수>
# https://www.acmicpc.net/problem/2193

n=int(input())
if n<3: print(1)
else:
    a,b=1,1
    for i in range(2,n):
        a,b=b,a+b
    print(b)