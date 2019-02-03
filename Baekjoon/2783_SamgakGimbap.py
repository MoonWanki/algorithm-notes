# BACKJOON #2783 <삼각 김밥>
# https://www.acmicpc.net/problem/2783

# 첫째 줄에 세븐25의 삼각 김밥 가격 정보 X와 Y가 주어진다. (Y그램 당 X원)
# 둘째 줄에는 세븐25를 제외한 편의점의 개수 N이 주어진다.
# 다음 N개의 줄에는 i번째 편의점의 삼각 김밥 가격 정보 Xi와 Yi가 주어진다. (Yi그램 당 Xi원)
# 첫째 줄에 삼각 김밥 1,000그램 가격의 최저가를 출력한다. 정답과의 오차는 0.01까지 허용한다.

a=[map(int,input().split())]
a+=[map(int,input().split())for i in' '*int(input())]
a=map(lambda x:x[0]/x[1],map(list,a))
print(min(a)*1000)