# BACKJOON #15650 <N과 M (2)>
# https://www.acmicpc.net/problem/15650

import itertools
n,m=map(int, input().split())
[print(*e) for e in itertools.combinations(range(1,n+1),m)]