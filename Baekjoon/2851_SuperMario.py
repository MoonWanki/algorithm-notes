# BACKJOON #2851 <슈퍼 마리오>
# https://www.acmicpc.net/problem/2851

arr = [int(input()) for i in range(10)]
score = 0
for n in arr:
	temp = score + n
	if temp >= 100:
		if temp-100 > 100-score:
			print(score)
		else: print(temp)
		exit()
	else: score = temp
print(score)
