# BACKJOON #15651 <N과 M (3)>
# https://www.acmicpc.net/problem/15651

import itertools
n,m=map(int, input().split())
[print(*e) for e in itertools.product(range(1,n+1), repeat=m)]