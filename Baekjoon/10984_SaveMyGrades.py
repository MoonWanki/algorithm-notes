# BACKJOON #10984 <내 학점을 구해줘>
# https://www.acmicpc.net/problem/10984

for _ in ' '*int(input()):
    sc,sg=0,0
    for _ in ' '*int(input()):
        c,g=map(float,input().split())
        sc+=c
        sg+=c*g
    sg=sg/sc
    print(int(sc),round(sg,1))
