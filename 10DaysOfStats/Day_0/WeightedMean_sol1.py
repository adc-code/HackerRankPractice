size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

total = 0;
weightTotal = 0;
for i in range (size):
    total += numbers[i] * weights[i]
    weightTotal += weights[i]

weightedMean = 0
if weightTotal != 0:
    weightedMean = total / weightTotal

print (round(weightedMean,1))


