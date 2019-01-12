# BACKJOON #2822 <점수 계산>
# https://www.acmicpc.net/problem/2822

a = sorted(sorted([ (i+1,int(input())) for i in range(8) ], key=lambda x:x[1], reverse=1)[0:5], key=lambda x:x[0])
print(sum(e[1] for e in a))
[ print(e[0], end=' ') for e in a ]