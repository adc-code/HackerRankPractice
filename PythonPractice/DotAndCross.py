import numpy

N = int(input())

tmp = []
for n in range(N):
    tmp.append(list(map(int,input().split())))
A = numpy.array(tmp)

tmp = []
for n in range(N):
    tmp.append(list(map(int,input().split())))
B = numpy.array(tmp)

print (A.dot(B))


