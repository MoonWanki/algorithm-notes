# BACKJOON #5567 <결혼식>
# https://www.acmicpc.net/problem/5567

n,m=int(input()),int(input())
a,r=[[0]*n for _ in' '*n],[0]*n
for _ in' '*m:
    x,y=map(int,input().split())
    a[x-1][y-1]=a[y-1][x-1]=1
for i in range(n):
    if a[0][i]:
        r[i]=1
        r=list(map(sum,zip(a[i],r)))
print(n-r.count(0)-1)