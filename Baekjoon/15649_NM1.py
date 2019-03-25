# BACKJOON #15649 <N과 M (1)>
# https://www.acmicpc.net/problem/15649

import itertools
n,m=map(int, input().split())
[print(*e) for e in itertools.permutations(range(1,n+1),m)]