# BACKJOON #2810 <컵홀더>
# https://www.acmicpc.net/problem/2810

n = int(input())
seats = input()
count = 1
for seat in seats:
    if seat=='S': count = count + 1
    else: count = count + 0.5
if n < count: print(n)
else: print(int(count))