def print_rangoli(size):
    maxLength = 4 * (size-1) + 1

    for j in range(size, 0, -1):
        line = []
        for i in range(size, j, -1):
            let = (chr(ord('a') - 1 + i))
            line.append (chr(ord('a') - 1 + i))
        for i in range(j, size+1):
            let = (chr(ord('a') - 1 + i))
            line.append (chr(ord('a') - 1 + i))
        
        line = '-'.join(line)
        padding = '-' * int ((maxLength - len(line)) // 2)
        print (padding + line + padding)

    for j in range(2, size+1):
        line = []
        for i in range(size, j, -1):
            let = (chr(ord('a') - 1 + i))
            line.append (chr(ord('a') - 1 + i))
        for i in range(j, size+1):
            let = (chr(ord('a') - 1 + i))
            line.append (chr(ord('a') - 1 + i))
        
        line = '-'.join(line)
        padding = '-' * int ((maxLength - len(line)) // 2)
        print (padding + line + padding)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

