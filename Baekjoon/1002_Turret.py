# BACKJOON #1002 <Turret>
# https://www.acmicpc.net/problem/1002

import math
for _ in' '*int(input()):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d:
        if d>r1+r2: print(0)
        elif d==r1+r2: print(1)
        elif r1>d+r2 or r2>d+r1: print(0)
        elif r1==d+r2 or r2==d+r1: print(1)
        else: print(2)
    else:
        if r1-r2: print(0)
        else: print(-1)