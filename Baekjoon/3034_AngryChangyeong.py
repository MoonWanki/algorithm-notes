# BACKJOON #3034 <앵그리 창영>
# https://www.acmicpc.net/problem/3034

n,w,h=map(int,input().split(' '))
[print('NE'if int(input())**2>w**2+h**2 else'DA')for _ in' '*n]