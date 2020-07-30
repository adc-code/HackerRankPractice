NumTests = int(input())

for n in range(NumTests):
    _ = input()
    SetA = set(map(int, input().split()))

    _ = input()
    SetB = set(map(int, input().split()))

    print (SetA.issubset(SetB))



