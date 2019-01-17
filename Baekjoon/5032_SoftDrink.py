# BACKJOON #5032 <탄산 음료>
# https://www.acmicpc.net/problem/5032

e,f,c=map(int,input().split(' '))
r,n=e+f,0
while r>=c:
    a=r//c
    r-=c*a-a
    n+=a
print(n)