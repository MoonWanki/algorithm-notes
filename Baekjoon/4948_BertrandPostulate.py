# BACKJOON #4948 <베르트랑 공준>
# https://www.acmicpc.net/problem/4948

isPrime = [True]*250000
for n in range(2, 250000):
    if n:
        i = n*2
        while i < 250000:
            isPrime[i] = False
            i = i + n

def numPrimes(n):
    if n == 1: return 1
    count = 0
    for i in range(n, 2*n):
        if isPrime[i+1]: count = count + 1
    return count

while True:
    n = int(input())
    if n==0: break
    print(numPrimes(n))