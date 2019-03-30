# BACKJOON #3015 <오아시스 재결합>
# https://www.acmicpc.net/problem/3015

# 오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.
# 이 역사적인 순간을 맞이하기 위해 줄에서서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해 졌다.
# 두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.
# 줄에 서있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.

s,c=[],0
for i in range(int(input())):
    h=int(input())
    while True:
        if len(s)==0:
            s.append([h, 1])
            break
        elif s[-1][0] < h:
            c+=s[-1][1]
            s.pop()
        elif s[-1][0] == h:
            c+=s[-1][1]
            s[-1][1]+=1
            if len(s)>1: c+=1
            break
        else:
            c+=1
            s.append([h, 1])
            break
print(c)