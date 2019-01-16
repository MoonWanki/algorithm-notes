# BACKJOON #2156 <포도주 시식>
# https://www.acmicpc.net/problem/2156

a = [ int(input()) for _ in ' '*int(input()) ]
if len(a) < 3: print(sum(a))
else:
    m1,m2,m3=0,a[0],a[0]+a[1]
    for i in range(2,len(a)):
        m1,m2,m3=m2,m3,max(m1+a[i-1]+a[i],m2+a[i],m3)
    print(m3)