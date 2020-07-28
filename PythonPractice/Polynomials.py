import numpy

coefs = list(map(float,input().split()))
val   = int(input())

print (numpy.polyval(coefs, val))


