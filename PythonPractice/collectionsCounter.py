# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

numOfShoes = int(input())

shoeCount = collections.Counter (list(map(int, input().split())))

numCustomers = int(input())

totalMoney = 0;
for cust in range (numCustomers):
    shoeSize, cost = map(int,input().split())
    if (shoeCount[shoeSize] > 0):
        totalMoney += cost
        shoeCount[shoeSize] -= 1

print(totalMoney)


