if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    X = range (0, x+1)
    Y = range (0, y+1)
    Z = range (0, z+1)

    results = [ [a,b,c] for a in X for b in Y for c in Z if a + b + c != n ]

    print (results)


