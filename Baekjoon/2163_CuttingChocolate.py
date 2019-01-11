# BACKJOON #2193 <초콜릿 자르기>
# https://www.acmicpc.net/problem/2193

arr=[[0 for j in range(301)]for i in range(301)]
for i in range(1, 301):
    arr[1][i] = arr[i][1] = i-1
for i in range(2, 301):
    for j in range(2, 301):
        if i<j:
            k=j//2
            l=j-k
            arr[i][j] = arr[i][k] + arr[i][l] + 1
        else:
            k=i//2
            l=i-k
            arr[i][j] = arr[k][j] + arr[l][j] + 1
n,m = list(map(int, input().split(' ')))
print(arr[n][m])