import re

N = int(input())

for _ in range(N):
    result = bool (re.match(r'^[789]\d{9}$', input()))
    if result:
        print ('YES')
    else:
        print ('NO')



