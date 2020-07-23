N = int(input())

xValues = list(map(float, input().split()))
yValues = list(map(float, input().split()))

xValues_sorted = xValues.copy()
xValues_sorted.sort()

yValues_sorted = yValues.copy()
yValues_sorted.sort()

totalDi2 = 0
for i in range(N):
    xRank = xValues_sorted.index (xValues[i]) + 1
    yRank = yValues_sorted.index (yValues[i]) + 1    

    d_i = xRank - yRank
    totalDi2 += d_i ** 2

r = 1 - (6 * totalDi2) / (N * (N ** 2 - 1))

print (round(r,3))
