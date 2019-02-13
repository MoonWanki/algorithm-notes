# BACKJOON #11404 <플로이드>
# https://www.acmicpc.net/problem/11404

n=int(input())
a=[[float('inf')]*n for _ in' '*n]
for _ in' '*int(input()):
    x,y,c=map(int,input().split())
    a[x-1][y-1]=min(a[x-1][y-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j]=min(a[i][j], a[i][k]+a[k][j]) if i!=j else 0
for i in range(n):
    for j in range(n):
        print(a[i][j] if a[i][j]!=float('inf') else 0, end=' ')
    print()