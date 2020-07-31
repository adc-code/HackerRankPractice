# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
#print (sorted(S))
upper = []
lower = []
odds  = []
evens = []

for c in S:
    if c.isupper():
        upper.append (c)
    elif c.islower():
        lower.append (c)
    elif c.isdigit():
        if int(c) % 2 == 1:
            odds.append(c)
        else:
            evens.append(c)

print ( "".join(sorted(lower)) + "".join(sorted(upper)) + "".join(sorted(odds)) + "".join(sorted(evens)) )    


