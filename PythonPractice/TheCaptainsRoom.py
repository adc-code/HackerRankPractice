_ = input ()

data = list (map(int, input().split()))

roomCount = {}
for i in data:
    if i not in roomCount:
        roomCount[i] = 1
    else:
        roomCount[i] = roomCount[i] + 1

for item in roomCount.keys():
    if roomCount[item] == 1:
        print (item)
        break


