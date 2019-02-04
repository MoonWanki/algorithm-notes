# BACKJOON #10409 <서버>
# https://www.acmicpc.net/problem/10409

# 당신은 FCFS(First-Come, First-Served)의 규칙에 따라 요청된 일을 처리하는 서버를 담당하게 되었다.
# 매일, 당신은 일을 처리하기 위해 최대 T분 동안 서버에 시간을 할당할 수 있다.
# 당신은 오늘 주어진 시간동안 몇개의 일이 완료될 수 있는지 알고싶다.

# 첫 줄은 두 정수 n과 T이며 (1 ≤ n ≤ 50, 1 ≤ T ≤ 500) n은 일의 개수를 나타낸다.
# 두 번째 줄은 n개의 100 이하인 자연수가 입력되며, 입력된 각 일의 수행 시간을 나타낸다.

n,T=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    T-=a[i]
    if T<0:
        print(i)
        break
if T>0: print(n)