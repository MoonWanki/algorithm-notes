# BACKJOON #5618 <공약수>
# https://www.acmicpc.net/problem/5618

import math,functools;input();x=functools.reduce(math.gcd,list(map(int,input().split())));[print(i)for i in range(1,x+1) if x%i==0]
