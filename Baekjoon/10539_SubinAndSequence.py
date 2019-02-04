# BACKJOON #10539 <수빈이와 수열>
# https://www.acmicpc.net/problem/10539

# 수빈이는 심심해서 수열을 가지고 놀고 있다.
# 먼저, 정수 수열 A를 쓴다. 그리고 그 아래에 정수 수열 A의 해당 항까지의 평균값을 그 항으로 하는 정수 수열 B를 쓴다. 
# 예를 들어, 수열 A가 1, 3, 2, 6, 8이라면, 수열 B는 1/1, (1+3)/2, (1+3+2)/3, (1+3+2+6)/4, (1+3+2+6+8)/5, 즉, 1, 2, 2, 3, 4가 된다. 
# 수열 B가 주어질 때, 수빈이의 규칙에 따른 수열 A는 뭘까?

n=int(input())
a=list(map(int,input().split()))
b=[a[0]]*n
for i in range(1,n):
    s=a[i]*(i+1)
    b[i]=s-sum(b[:i])
[print(w,end=' ')for w in b]