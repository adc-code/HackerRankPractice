import math

N = int(input())
X_Values = list(map(float, input().split()))
Y_Values = list(map(float, input().split()))

mean_X = sum (X_Values) / N
mean_Y = sum (Y_Values) / N

SD_X = 0
SD_Y = 0
CoVar = 0
for i in range(N):
    SD_X  += (X_Values[i] - mean_X) ** 2
    SD_Y  += (Y_Values[i] - mean_Y) ** 2
    CoVar += (X_Values[i] - mean_X) * (Y_Values[i] - mean_Y)

SD_X = (SD_X / N) ** 0.5
SD_Y = (SD_Y / N) ** 0.5

Pearson = CoVar / (N * SD_X * SD_Y)

print (round(Pearson,3))


