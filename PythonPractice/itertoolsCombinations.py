from itertools import combinations

inputStr, k = input().split()
k = int(k)
inputStr = sorted(str(inputStr))

results = []
for length in range (1, k+1):
    currResults = []

    combos = list(combinations(inputStr, length))
    for i in combos:
        currResults.append (''.join(i))

    currResults.sort ()
    results.extend(currResults)


for i in results:
    print (i)


