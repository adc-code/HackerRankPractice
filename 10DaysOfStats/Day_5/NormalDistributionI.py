import math

mean = 20
SD   = 2

P_1 = 0.5 * (1 + math.erf ( (19.5 - mean)/(SD * 2 ** 0.5)))
P_2 = 0.5 * (1 + math.erf ( (22 - mean)/(SD * 2 ** 0.5))) - 0.5 * (1 + math.erf ( (20 - mean)/(SD * 2 ** 0.5)))

print (round(P_1, 3))
print (round(P_2, 3))


