if __name__ == '__main__':
    data = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        data.append ([name, score])
        scores.add (score)

    scores = list(scores)
    scores.sort ()

    Lowest2 = scores[1]

    LowestNameList = []
    for student in data:
        if student[1] == Lowest2:
            LowestNameList.append (student[0])

    LowestNameList.sort ()

    for name in LowestNameList:
        print (name)


