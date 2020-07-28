import numpy

N, M = map(int,input().split())

a = []
b = []

for n in range(N):
    a.append(list(map(int,input().split())))

for n in range(N):
    b.append(list(map(int,input().split())))

print (numpy.add(a, b))
print (numpy.subtract(a, b))
print (numpy.multiply(a, b))
print (numpy.floor_divide(a, b))
print (numpy.mod(a, b))
print (numpy.power(a, b))


