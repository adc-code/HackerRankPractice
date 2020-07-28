import numpy

N = int(input())

data = []
for n in range(N):
    data.append (list(map(float,input().split())))

arr = numpy.array (data)

#print (arr)
print (round(numpy.linalg.det (arr),2))



