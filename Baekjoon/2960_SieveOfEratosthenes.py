# BACKJOON #2960 <에라토스테네스의 체>
# https://www.acmicpc.net/problem/2960

N,K = input().split(' ')
N,K = int(N),int(K)
arr = [True]*N*2
for n in range(2, N+1):
    i = n
    while i <= N:
        if arr[i]:
            K -= 1
            if not K: print(i)
            arr[i] = False
        i += n