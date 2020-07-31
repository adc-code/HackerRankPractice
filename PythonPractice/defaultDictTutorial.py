# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

n, m = map(int, input().split())

listN = list ()
for i in range(n):
    listN.append(input())

data = collections.defaultdict (list)
for i in range(n):
    #print (listN[i])
    #data['a'].append(i+1)
    data[listN[i]].append (i+1)

listM = list ()
for i in range(m):
    listM.append(input())

for i in listM:
    #print (i)
    if i in data:
        print (" ".join (map(str,data[i]) ))
    else:
        print (-1) 

#(data[listM[i]].items())


