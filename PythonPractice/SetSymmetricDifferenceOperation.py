_ = input()
SetA = set (map(int, input().split()))

_ = input()
SetB = set (map(int, input().split()))

print (len(SetA.symmetric_difference(SetB)))



