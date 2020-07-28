import numpy

N, M = map(int, input().split())

data = []
for i in range(N):
    data.append (list(map(int, input().split())))

arr = numpy.array (data)
print (numpy.transpose(arr))
print (arr.flatten())


