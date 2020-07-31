# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
ColNames = list(map(str,input().split()))
idx = (ColNames.index('MARKS'))

total = 0;
for i in range(N):
    tmp = list(map(str,input().split()))
    total += int(tmp[idx])

print (total / N)



