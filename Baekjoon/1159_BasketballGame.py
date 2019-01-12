# BACKJOON #1159 <농구 경기>
# https://www.acmicpc.net/problem/1159

a=[input() for _ in ' '*int(input())]
b=[0]*26
for s in a:
    b[ord(s[0])-97]+=1
s=''
for i,n in enumerate(b):
    if n>4: s+=chr(i+97)
print(s if len(s) else 'PREDAJA')