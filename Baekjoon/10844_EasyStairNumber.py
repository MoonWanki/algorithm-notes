# BACKJOON #10844 <쉬운 계단 수>
# https://www.acmicpc.net/problem/10844

n = int(input())
if n==1: print(9)
else:
    a = [0]+[1]*9
    for i in range(n-1):
        b=[0]*10
        b[1]+=a[0]
        for i in range(1,9):
            b[i-1]+=a[i]
            b[i+1]+=a[i]
        b[8]+=a[9]
        a=b
    print(sum(a)%1000000000)