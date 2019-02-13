# BACKJOON #3023 <마술사 이민혁>
# https://www.acmicpc.net/problem/3023

r,c=map(int,input().split())
a=[[0]*2*c for _ in' '*2*r]
for i in range(r):
    for j,c in enumerate(input()):
        a[i][j]=a[-i-1][j]=a[i][-j-1]=a[-i-1][-j-1]=c
x,y=map(int,input().split())
a[x-1][y-1]='#'if a[x-1][y-1]=='.'else'.'
for r in a:
    for c in r:
        print(c,end='')
    print()