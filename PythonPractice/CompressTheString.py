from itertools import groupby

testData = input ()

# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

print (*[ (len(list(g)), int(k)) for k, g in groupby(testData)])


