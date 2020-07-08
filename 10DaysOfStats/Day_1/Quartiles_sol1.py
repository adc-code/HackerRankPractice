def FindMedian (values):

    indices = []
    median  = 0

    if len (values) % 2 == 1:
        
        indices.append (len (values) // 2)
        median = values [ int (len (values) // 2) ]

    else:

        indices.append ( int (len (values) / 2) )
        indices.append ( int (len (values) / 2 - 1) )
        median = int (0.5 * (values [ indices [0] ] + values [ indices[1] ]))

    return (median, indices)



N = int(input())
Nums = list (map(int, input().split()))
Nums.sort ()


median, medianIndices = FindMedian (Nums)
Q1, _ = FindMedian (Nums[:medianIndices[0]])
Q3, _ = FindMedian (Nums[(medianIndices[-1] + 1):])

print (Q1)
print (median)
print (Q3)

    
