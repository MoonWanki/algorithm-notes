# BACKJOON #1158 <조세퍼스 문제>
# https://www.acmicpc.net/problem/1158

n,m=map(int,input().split())
t=0
a=list(range(1,n+1))
r=[]
while len(a):
    t=(t+m-1)%len(a)
    r.append(a.pop(t))
print('<',end='')
[print('{},'.format(n),end=' ')for n in r[:-1]]
print('{}>'.format(r[-1]))