import numpy

def arrays(arr):
    arr.reverse()
    return numpy.array(list(map(float,arr)),float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


