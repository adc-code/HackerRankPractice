_ = input ()

arrayN = list(map(int, input().split()))

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness = 0
for n in arrayN:
    if n in setA:
        happiness += 1

    if n in setB:
        happiness -= 1

print (happiness)


