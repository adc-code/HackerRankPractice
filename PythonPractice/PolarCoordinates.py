# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


if __name__ == '__main__':
    n = complex(input())

    print (abs(n))
    print (cmath.phase(n))

