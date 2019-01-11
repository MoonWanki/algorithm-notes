# BACKJOON #5063 <TGN>
# https://www.acmicpc.net/problem/5063

for _ in range(int(input())):
    r,e,c = list(map(int, input().split(' ')))
    if e-c > r: print('advertise')
    elif e-c < r: print('do not advertise')
    else: print('does not matter')