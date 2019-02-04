# BACKJOON #1788 <피보나치 수의 확장>
# https://www.acmicpc.net/problem/1788

# 피보나치 수 F(n)을 n이 음수인 경우로도 확장시킬 수 있다.
# 예를 들어 n=1일 때 F(1)=F(0)+F(-1)이 성립되어야 하므로, F(-1)은 1이 되어야 한다.
# n이 주어졌을 때, 피보나치 수 F(n)을 구하는 프로그램을 작성하시오. n은 음수로 주어질 수도 있다.

n=int(input())
if n==0: print("0\n0")
else:
    print(-1 if n<0 and -n%2==0 else 1)
    n=abs(n)
    a,b=0,1
    for _ in' '*(n-1):
        a,b=b,(a+b)%1000000000
    print(b)