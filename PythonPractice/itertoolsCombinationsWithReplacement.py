from itertools import combinations_with_replacement

inputStr, k = input().split()
k = int(k)


results = list(combinations_with_replacement (sorted(inputStr), k))

#print (results)
strResults = []
for i in results:
    strResults.append (''.join(i))

strResults.sort()
#print(strResults)

for i in strResults:
    print (i)


