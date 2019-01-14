# BACKJOON #2798 <블랙잭>
# https://www.acmicpc.net/problem/2798

n,m=map(int,input().split(' '))
a=list(map(int,input().split(' ')))
a.sort()
a.reverse()
max=0
for i in range(0,n-2):
    if a[i]>m: continue
    for j in range(i+1,n-1):
        if a[i]+a[j]>m: continue
        for k in range(j+1,n):
            s=a[i]+a[j]+a[k]
            if s>m: continue
            max=s if s>max else max
print(max)