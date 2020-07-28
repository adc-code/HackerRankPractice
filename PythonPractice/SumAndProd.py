import numpy

N, M = map(int,input().split())

data = []
for n in range(N):
    data.append(list(map(int,input().split())))

print(numpy.prod(numpy.sum(data,axis=0)))


