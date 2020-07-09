q = 2/3
p = 1 - q

g = 0

for i in range (0, 5):
    g += q**i * p

print (round(g, 3))
