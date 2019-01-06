# BACKJOON #5565 <영수증>
# https://www.acmicpc.net/problem/5565

sum = int(input())
for i in range(9):
    sum = sum - int(input())
print(sum)