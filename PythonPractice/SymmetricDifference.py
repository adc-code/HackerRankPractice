_ = input()
MList = list(map(int, input().split()))
MSet = set(MList)

_ = input()
NList = list(map(int, input().split()))
NSet = set(NList)

diffMN = MSet.difference (NSet)
diffNM = NSet.difference (MSet)

#print (diffMN)
#print (diffNM)

diffs = list (diffMN)
diffs.extend (list(diffNM))

#print (diffs)
diffs.sort ()

for i in diffs:
    print (i)


