import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int,input().split())

data = []
for n in range(N):
    data.append(list(map(int,input().split())))

print(numpy.mean(data,axis=1))
print(numpy.var(data,axis=0))
print(numpy.std(data,axis=None))



