inputLine = input().split()
N = int(inputLine[0])
M = int(inputLine[1])

for i in range(1, N//2 + 1):
    p = (2*i - 1) * '.|.'
    b = (M - len(p)) // 2 * '-'
    print (b + p + b)

p = 'WELCOME'
b = (M - len(p)) // 2 * '-'
print (b + p + b)

for i in range(N//2, 0, -1):
    p = (2*i - 1) * '.|.'
    b = (M - len(p)) // 2 * '-'
    print (b + p + b)    


