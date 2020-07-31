# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

testNum = int(input())


for t in range(testNum):
    N = int(input())
    cubes = collections.deque(map(int,input().split()))

    cubeStack = []
    didIt = "Yes"
    while len(cubes) > 0:
        if len(cubeStack) == 0:
            if cubes[0] >= cubes[-1]:
                cubeStack.append (cubes[0])
                cubes.popleft ()
            else:
                cubeStack.append (cubes[-1])
                cubes.pop ()
            #print ("empty cube stack")
            #print (cubes)
            #print (cubeStack)
        else:
            #print ("regular case")
            #print (cubes)
            #print (cubeStack)
            if (cubes[0] >= cubes[-1] and cubes[0] <= cubeStack[-1]):
                cubeStack.append(cubes[0])
                cubes.popleft()
            elif (cubes[-1] > cubes[0] and cubes[-1] <= cubeStack[-1]):
                cubeStack.append(cubes[-1])
                cubes.pop()
            else:
                didIt = "No"
                break

            #print (cubes)
            #print (cubeStack)

    print (didIt)


