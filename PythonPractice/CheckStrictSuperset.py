SetA = set(map(int, input().split()))

N = int(input())

isSS = True

for _ in range(N):
    SetB = set(map(int, input().split()))

    result = SetA.issuperset(SetB)
    if not result:
        isSS = result
        break

print (isSS)


