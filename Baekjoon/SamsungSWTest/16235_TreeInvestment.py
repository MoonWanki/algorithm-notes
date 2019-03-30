# BACKJOON #16235 <나무 재테크>
# https://www.acmicpc.net/problem/16235

from functools import reduce
import heapq
N,M,K=map(int,input().split())
land=[[{ 'value':5, 'trees':[] } for _ in ' '*N] for _ in ' '*N]
A=[list(map(int, input().split())) for _ in ' '*N]

for _ in range(M):
    x,y,old=map(int,input().split())
    heapq.heappush(land[x-1][y-1]['trees'], old)

# [print(r) for r in land]

for y in range(K):

    # SS
    # print(y, '- SS')
    for r in land:
        for e in r:
            value, trees = 0, e['trees']
            newTrees = []
            while trees:
                youngestTree = heapq.heappop(trees)
                if e['value'] >= youngestTree:
                    e['value'] -= youngestTree
                    youngestTree += 1
                    heapq.heappush(newTrees, youngestTree)
                else: 
                    value += youngestTree//2
            e['value'], e['trees'] = e['value'] + value, newTrees
    # [print(r) for r in land]

    # FW
    # print(y, '- FW')
    for i, r in enumerate(land):
        for j, e in enumerate(r):
            land[i][j]['value']+=A[i][j]
            dv = len(list(filter(lambda x: x%5==0, e['trees'])))
            if not dv:
                continue
            for dx, dy in (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1):
                dx+=i; dy+=j
                if 0 <= dx < N and 0 <= dy < N:
                    [heapq.heappush(land[dx][dy]['trees'], 1) for _ in range(dv)]
    # [print(r) for r in land]

sum=0
for r in land:
    for e in r:
        sum+=len(e['trees'])
print(sum)