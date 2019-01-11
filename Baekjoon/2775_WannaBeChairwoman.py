# BACKJOON #2775 <부녀회장이 될테야>
# https://www.acmicpc.net/problem/2775

arr = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for i in range(14):
    tarr = [0]
    for j in range(14):
        tarr.append(tarr[j]+arr[i][j+1])
    arr.append(tarr)
        
for i in range(int(input())):
    print(arr[int(input())][int(input())])