# BACKJOON #12790 <Mini Fantasy War>
# https://www.acmicpc.net/problem/12790

for _ in '_'*int(input()):
    arr = list(map(int, input().split(' ')))
    for i in range(4):
        arr[i]+=arr[i+4]
    arr[0] = arr[0] if arr[0]>1 else 1
    arr[1] = arr[1] if arr[1]>1 else 1
    arr[2] = arr[2] if arr[2]>0 else 0
    print(arr[0]+5*arr[1]+2*arr[2]+2*arr[3])