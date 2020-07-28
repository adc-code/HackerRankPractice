N = int(input())

    data = []
    for _ in range(N):

        line = input().split()

        if line[0] == 'insert':
            data.insert (int(line[1]), int(line[2]))
        elif line[0] == 'print':
            print (data)
        elif line[0] == 'remove':
            data.remove (int(line[1]))
        elif line[0] == 'append':
            data.append (int(line[1]))
        elif line[0] == 'sort':
            data.sort ()
        elif line[0] == 'pop':
            data.pop ()
        elif line[0] == 'reverse':
            data.reverse ()


