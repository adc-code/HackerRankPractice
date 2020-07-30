def swap_case(s):

    newS = []
    for l in s:
        x = l
        if l.islower ():
            x = l.upper()
        elif l.isupper ():
            x = l.lower()

        newS.append (x)

    return ''.join (newS)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


