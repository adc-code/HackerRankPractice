N = int(input())
Nums = list (map(int, input().split()))

# find the mean
total = 0
for n in Nums:
    total += n

mean = total / N

# find the variance
variance = 0;
for n in Nums:
    variance += (n - mean) ** 2

variance /= N

stdDev = variance ** 0.5

print (f'{stdDev:.1f}')
    
