# BACKJOON #11052 <카드 구매하기>
# https://www.acmicpc.net/problem/11052

n=int(input())
p=list(map(int,input().split()))
a=[[0]*(n+1) for _ in' '*(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<i: a[i][j] = a[i-1][j]
        else: a[i][j] = max(a[i-1][j], a[i][j-i]+p[i-1])
print(a[n][n])