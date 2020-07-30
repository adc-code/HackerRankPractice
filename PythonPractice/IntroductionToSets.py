def average(array):
    distinctHeights = set (array)
    return (sum(distinctHeights) / len(distinctHeights)) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


