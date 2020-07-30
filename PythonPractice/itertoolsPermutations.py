from itertools import permutations

inputStr, k = input().split()
k = int(k)

permutes = list(permutations(inputStr, k))
results = []
for i in permutes:
    results.append (''.join(i))

results.sort()
for i in results:
    print (i)



