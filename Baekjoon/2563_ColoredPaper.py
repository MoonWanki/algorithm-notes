# BACKJOON #2563 <색종이>
# https://www.acmicpc.net/problem/2563

arr=[[0 for _ in '_'*100] for _ in '_'*100]
for _ in '_'*int(input()):
    x,y = list(map(int, input().split(' ')))
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1
s=0
for a in arr:
    s += a.count(1)
print(s)