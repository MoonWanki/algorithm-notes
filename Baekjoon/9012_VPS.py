# BACKJOON #9012 <괄호>
# https://www.acmicpc.net/problem/9012

t=input()
for i in range(int(t)):
    n=0
    s=input()
    for c in s:
        if c=='(': n=n+1
        else:
            n=n-1
            if n<0: break
    if n==0: print('YES')
    else: print('NO')