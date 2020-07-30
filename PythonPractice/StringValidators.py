if __name__ == '__main__':
    s = input()
    results = [ False, False, False, False, False ]
    for char in s:
        results[0] = results[0] or char.isalnum()
        results[1] = results[1] or char.isalpha()
        results[2] = results[2] or char.isdigit()
        results[3] = results[3] or char.islower()
        results[4] = results[4] or char.isupper()

    for res in results:
        print (res)


