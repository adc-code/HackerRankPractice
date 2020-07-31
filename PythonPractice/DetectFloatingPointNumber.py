import re

N = int(input())

for _ in range(N):
    print ( bool (re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())) )


