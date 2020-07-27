# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = int(input())
y = int(input())

a = 0.5 * (x ** 2 + y ** 2) ** 0.5
b = 0.5 * y

print (str( int(round(math.degrees(math.acos(b/a)),0)) )+'\u00b0')

