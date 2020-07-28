import numpy

data = list(map(float,input().split()))

arr = numpy.array (data)

numpy.set_printoptions(sign=' ')

print ((numpy.floor(arr)))
print ((numpy.ceil(arr)))
print ((numpy.rint(arr)))


