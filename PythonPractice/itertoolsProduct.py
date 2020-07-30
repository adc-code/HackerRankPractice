from itertools import product

SetA = set(map(int, input().split()))
SetB = set(map(int, input().split()))

print (*list(product(SetA, SetB)))


