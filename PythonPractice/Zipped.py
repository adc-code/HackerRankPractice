# Enter your code here. Read input from STDIN. Print output to STDOUT

studs, subs = map(int,input().split())

grades = []
for s in range(subs):
    tmp = list(map(float,input().split()))
    grades.append (tmp)

X = list(zip(*grades))

#print (X)

for i in X:
    print (sum(i) / len(i))


