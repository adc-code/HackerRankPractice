import math

p = 1.09/2.09  # boys over (boys + girls)
q = 1 - p    

N = 6

results = 0;

for x in range (3, N+1):
     
    results += math.factorial(N) / (math.factorial(x) * math.factorial(N-x)) * p ** x * q ** (N - x)

print (round(results,4))
