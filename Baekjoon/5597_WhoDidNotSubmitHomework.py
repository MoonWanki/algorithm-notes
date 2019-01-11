# BACKJOON #5597 <과제 안 내신 분..?>
# https://www.acmicpc.net/problem/5597

a=list(range(1,31))
for _ in '_'*28:
    a.remove(int(input()))
a.sort()
[print(n) for n in a]