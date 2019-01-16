# BACKJOON #5532 <방학 숙제>
# https://www.acmicpc.net/problem/5532

L,A,B,C,D=[int(input()) for _ in' '*5]
while A>0 or B>0:
    L-=1
    A-=C
    B-=D
print(L)