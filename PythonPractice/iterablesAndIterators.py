from itertools import combinations

_ = input ()

letters = list (input().split())
k = int(input())

comboResults = list(combinations(letters, k))

aCount = 0
for i in comboResults:
    if 'a' in i:
        aCount += 1

print (aCount / len(comboResults))


