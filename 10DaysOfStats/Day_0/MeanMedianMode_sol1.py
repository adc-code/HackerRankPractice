N = int(input())

values = list (map(int, input().split()))

# compute the mean
total = 0;
for i in range (N):
    total += values [i]

mean = total / N


values.sort ()


# compute the median
median = 0;
if (N % 2 == 1):
    median = values [N // 2]
else:
    median = 0.5 * (values [N // 2] + values [(N // 2) - 1])


valueCounts = {}
for number in values:
    if number in valueCounts:
        valueCounts [number] = valueCounts [number] + 1
    else:
        valueCounts [number] = 1


mode = 0;
freq = 0;
for key, val in valueCounts.items():
    if val > freq:
        mode = key
        freq = val

# output results
print (mean)
print (median)
print (mode)


