import numpy

N, M, P = map(int,input().split())

data1 = []
data2 = []

for i in range(N):
    data1.append (list(map(int,input().split())))

for i in range(M):
    data2.append (list(map(int,input().split())))

arr1 = numpy.array (data1)
arr2 = numpy.array (data2)

print (numpy.concatenate((arr1, arr2), axis=0))


