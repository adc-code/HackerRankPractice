import math

Max = 9800
mean = 205
SD = 15
n = 49

mean_n = n * mean 
SD_n = n ** 0.5 * SD

Z = (Max - mean_n) / SD_n

P = 0.5 * (1 + math.erf (Z/(2 ** 0.5)) )
print (round(P,4))
