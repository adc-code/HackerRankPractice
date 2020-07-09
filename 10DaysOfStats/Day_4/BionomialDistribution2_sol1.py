import math

p = 0.12
q = 1 - p    

N = 10

# no more than 2... so 0, 1, or 2
results = 0;
for x in range (0, 3):
    results += math.factorial(N) / (math.factorial(x) * math.factorial(N-x)) * p ** x * q ** (N - x)
print (round(results,4))

# at least 2... so 2, 3, 4, ..., 10
results = 0;
for x in range (2, N+1):
    results += math.factorial(N) / (math.factorial(x) * math.factorial(N-x)) * p ** x * q ** (N - x)
print (round(results,4))



