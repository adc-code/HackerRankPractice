from itertools import product

K, M = [int(x) for x in input().split()]
arrayN = []
for _ in range(K):
    values = list(map(int, input().split()))
    arrayN.append(values[1:])

#print (arrayN)

possible_combinations = list(product(*arrayN))

#print (possible_combinations)

def func(nums):
    return sum([x ** 2 for x in nums]) % M

maxValue = 0
for combo in possible_combinations:
    result = func(combo)
    if result > maxValue:
        maxValue = result
        #print (maxValue, combo)

print (maxValue)
    
#print(max(list(map(func, possible_combinations))))


