# BACKJOON #6603 <로또>
# https://www.acmicpc.net/problem/6603

import itertools
while True:
    a=list(map(int,input().split()))
    if len(a)==1: break
    a=a[1:]
    for s in itertools.combinations(a, 6):
        [print(c,end=' ') for c in s]
        print('')
    print('')