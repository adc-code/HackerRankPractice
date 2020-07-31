# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

myDeque = collections.deque()

numOps = int(input())
for op in range(numOps):
    cmd = input().split()
    #print (cmd)
    if cmd[0] == 'append':
        myDeque.append(int(cmd[1]))
    elif cmd[0] == 'appendleft':
        myDeque.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        myDeque.pop()
    elif cmd[0] == 'popleft':
        myDeque.popleft()

    #print (myDeque)    

print (*myDeque)


