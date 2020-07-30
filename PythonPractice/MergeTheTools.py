def merge_the_tools(string, k):
    tStrings = []

    start = 0;
    #for i in range(0, k):
    for i in range(0, len(string)//k):
        tmp = string[start:(start+k)]
        start += k
        tStrings.append (tmp)

    #print (tStrings)
    for tStr in tStrings:
        uStr = ''
        for c in tStr:
            if c not in uStr:
                uStr += c

        print (uStr)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


