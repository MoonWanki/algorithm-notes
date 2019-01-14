# BACKJOON #10707 <수도요금>
# https://www.acmicpc.net/problem/10707

a,b,c,d,p=[int(input()) for _ in '_'*5]
x=a*p
y=b+(p>c)*(p-c)*d
print(x if x<y else y)