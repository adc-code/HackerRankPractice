import numpy

r, c = map(int,input().split())

data = []
for i in range(r):
    tmp = list(map(float,input().split()))
    data.append(tmp)

arr = numpy.array (data)
#print (arr)
m = numpy.min (arr, axis = 1)
print ( int(max(m)) )


