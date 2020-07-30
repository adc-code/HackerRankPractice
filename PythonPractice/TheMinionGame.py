def minion_game (string):
    # separate it into two lists...

    Score1 = 0  # Kevin
    Score2 = 0  # Stuart

    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            Score1 += (len(string) - i)
        else:
            Score2 += (len(string) - i)

    if Score1 > Score2:
        print ('Kevin', Score1)
    elif Score1 < Score2:
        print ('Stuart', Score2)
    else:
        print ('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)


