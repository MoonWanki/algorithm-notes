# BACKJOON #5596 <시험 점수>
# https://www.acmicpc.net/problem/5596

f=lambda:sum(map(int,input().split()))
a,b=f(),f()
print(b if b>a else a)