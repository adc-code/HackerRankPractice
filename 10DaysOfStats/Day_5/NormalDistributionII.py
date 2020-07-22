import math

mean = 70
SD   = 10

P_1 = 1 - 0.5 * (1 + math.erf ( (80 - mean)/(SD * 2 ** 0.5)))
P_2 = 1 - 0.5 * (1 + math.erf ( (60 - mean)/(SD * 2 ** 0.5)))
P_3 = 0.5 * (1 + math.erf ( (60 - mean)/(SD * 2 ** 0.5)))

print (round(100 * P_1,2))
print (round(100 * P_2,2))
print (round(100 * P_3,2))

