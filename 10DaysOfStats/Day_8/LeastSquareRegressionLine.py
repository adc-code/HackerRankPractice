Grades = []

for i in range(5):
    inputData = input().split()
    A, B = int(inputData[0]), int(inputData[1])

    Grades.append ( [A, B] )

n = len(Grades)

sum_x  = 0
sum_y  = 0
sum_xx = 0
sum_xy = 0
for grade in Grades:
    sum_xy += grade[0] * grade[1]
    sum_x  += grade[0]
    sum_y  += grade[1]
    sum_xx += grade[0] ** 2

b = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)

a = sum_y / n - b * sum_x / n

yval = a + 80 * b

print (round(yval, 3))


