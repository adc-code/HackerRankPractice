import math

Tics = 250

mean = 2.4
SD   = 2

N    = 100

N_mean = N * mean
N_SD   = N ** 0.5 * SD

P = 0.5 * (1 + math.erf ((Tics - N_mean) / (N_SD * 2 ** 0.5)))

print (round(P, 4))


