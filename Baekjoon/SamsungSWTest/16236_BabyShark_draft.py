N=int(input())
arr=[list(map(int, input().split())) for _ in' '*N]
sPos=None
sSize=2
sExp=0
time=0

def findNearestEatableFish():
    step=0
    global sPos
    queue = [sPos]
    visited = [[False]*N for _ in ' '*N]
    while True:
        step+=1
        nextQueue=[]
        for i,j in queue:
            if i>0 and not visited[i-1][j] and arr[i-1][j]<=sSize:
                visited[i-1][j] = True
                nextQueue.append((i-1,j))
            if j>0 and not visited[i][j-1] and arr[i][j-1]<=sSize:
                visited[i][j-1] = True
                nextQueue.append((i,j-1))
            if j<N-1 and not visited[i][j+1] and arr[i][j+1]<=sSize:
                visited[i][j+1] = True
                nextQueue.append((i,j+1))
            if i<N-1 and not visited[i+1][j] and arr[i+1][j]<=sSize:
                visited[i+1][j] = True
                nextQueue.append((i+1,j))
        print("nextQueue", nextQueue)
        if len(nextQueue)==0:
            return None, None
        nextQueue.sort()
        for i,j in nextQueue:
            if arr[i][j] > 0 and arr[i][j]<sSize:
                return step, (i, j)
        queue = nextQueue


for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            sPos = i,j
            break
    if sPos: break

while True:
    step, fPos = findNearestEatableFish()
    print(step, fPos)
    if not fPos: break
    
    arr[fPos[0]][fPos[1]] = 9
    arr[sPos[0]][sPos[1]] = 0
    sPos=fPos
    time+=step
    sExp+=1
    if sExp==sSize:
        sSize+=1
        sExp=0
    print('now', 'Lv', sSize, '{}/{}'.format(sExp,sSize))
    print(time, 's')
    print('---------------')
    [print(r) for r in arr]
    print('---------------')
print(time)