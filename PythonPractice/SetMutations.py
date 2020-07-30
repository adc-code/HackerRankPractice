_ = input ()

setA = set (map(int, input().split()))
numOps = int (input())

for _ in range (numOps):
    op = input().split()
    if op[0] == 'intersection_update':
        setB = set (map(int, input().split()))
        setA.intersection_update (setB)
    elif op[0] == 'update':
        setB = set (map(int, input().split()))
        setA.update (setB)
    elif op[0] == 'symmetric_difference_update':
        setB = set (map(int, input().split()))
        setA.symmetric_difference_update (setB)
    elif op[0] == 'difference_update':
        setB = set (map(int, input().split()))
        setA.difference_update (setB)
 
print (sum(setA))


