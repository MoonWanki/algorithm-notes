# BACKJOON #4153 <직각삼각형>
# https://www.acmicpc.net/problem/4153

while True:
    a=list(map(int,input().split()))
    if a[0]:
        m=max(a)
        a.remove(m)
        print("right"if sum([i**2 for i in a])==m**2 else"wrong")
    else: break