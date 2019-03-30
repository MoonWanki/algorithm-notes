# Programmers > 완전탐색 > 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, red):
    answer = []
    sum=brown//2 + 2
    for h in range(1, sum//2 + 1):
        w = sum-h
        if (w-2)*(h-2)==red:
            answer = [w,h]
            break
    return answer
