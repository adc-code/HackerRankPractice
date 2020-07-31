n = int(input())

arr = input().split(" ")

#print (list(i == i[::-1]for i in arr))
#for i in arr:
#    print (i + "  " + i[::-1])

print (all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))



