# Programmers > 스택/큐 > 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    q=[]
    for p,s in zip(progresses, speeds):
        t = (100-p)//s + 1
        if q and t<=q[-1]:
            answer[-1] += 1
        else:
            q.append(t)
            answer.append(1)
    return answer