# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for t in range(T):
    a, b = input().split()
    try:
        #print (a + " " + b)
        print (int(a) // int(b))
    except ZeroDivisionError as e:
        print ("Error Code: " + str(e))
    except ValueError as e:
        print ("Error Code: " + str(e))


