# BACKJOON #10929 <SHA-224>
# https://www.acmicpc.net/problem/10929

import hashlib
print(hashlib.sha224(str.encode(input())).hexdigest())