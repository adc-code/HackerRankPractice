# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

M, D, Y = map(int, input().split())

cal = calendar.monthcalendar (Y, M)

#print (cal)
dayNames = list (calendar.day_name)
#print (dayNames)

for week in cal:
    if D in week:
        idx = week.index(D)
        print (dayNames[idx].upper())


