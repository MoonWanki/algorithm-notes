# BACKJOON #11726 <2×n 타일링>
# https://www.acmicpc.net/problem/11726

a,b,n=0,1,int(input())
for _ in ' '*n:
    a,b=b,a+b
print(b/10007)