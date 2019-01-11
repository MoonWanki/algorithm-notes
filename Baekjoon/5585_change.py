# BACKJOON #5585 <거스름돈>
# https://www.acmicpc.net/problem/5585

c = 1000-int(input())
n=0
for t in [500,100,50,10,5,1]:
    while c>=t:
        c-=t
        n+=1
print(n)