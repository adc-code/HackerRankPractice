def FindMedian (values):

    indices = []
    median  = 0

    if len (values) % 2 == 1:
        
        indices.append (len (values) // 2)
        median = values [ int (len (values) // 2) ]

    else:

        indices.append ( int (len (values) / 2 - 1) )
        indices.append ( int (len (values) / 2) )

        median = 0.5 * (values [ indices [0] ] + values [ indices[1] ])

    return (median, indices)



N = int(input())
Nums = list (map(int, input().split()))
Freq = list (map(int, input().split()))

ActualNums = [];
for i in range (N):
    for j in range (Freq[i]):
        ActualNums.append (Nums[i])
ActualNums.sort ()


median, medianIndices = FindMedian (ActualNums)

if len(medianIndices) == 1:
    Q1, _ = FindMedian (ActualNums[:medianIndices[0]])
    Q3, _ = FindMedian (ActualNums[(medianIndices[0]+1):])
else:
    Q1, _ = FindMedian (ActualNums[:medianIndices[1]])
    Q3, _ = FindMedian (ActualNums[medianIndices[-2]:])

print (f'{range:.1f}')
    
