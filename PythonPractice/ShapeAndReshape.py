import numpy

data = list(map(int,input().split()))

arr = numpy.array (data)
print (numpy.reshape(arr,(3,3)))


