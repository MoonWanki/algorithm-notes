# BACKJOON #10886 <0 = not cute / 1 = cute>
# https://www.acmicpc.net/problem/10886

n,c=int(input()),0
for i in 'a'*n:
    if int(input()):c+=1
print("Junhee is "+"not "*(n/2>c) + "cute!")