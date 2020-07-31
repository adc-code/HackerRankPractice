# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

N = int(input())

oDict = collections.OrderedDict ()

for i in range(N):
    data = list(input().split())
    val = int(data[-1])
    name = " ".join (data[0:len(data)-1])

    if name in oDict.keys():
        oDict[name] += val
    else:
        oDict[name] = val

for k,v in oDict.items():
    print (str(k) + " " + str(v))



