# BACKJOON #10798 <세로읽기>
# https://www.acmicpc.net/problem/10798

a = [input() for i in 'a'*5]
for i in range(15):
    for s in a:
        if i<len(s):
            print(s[i],end='')