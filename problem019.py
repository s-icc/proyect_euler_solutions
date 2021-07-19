"""

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

from calendar import TextCalendar

cl = TextCalendar()
cl.setfirstweekday(6) # asigna como primer día de la semana a domingo

first_sunday = 0

for year in range(1901, 2001):
	for month in range(1, 13):
		month_of_the_year = cl.monthdayscalendar(year, month) # devuelve un array del mes con arrays de las semanas
		if month_of_the_year[0][0] == 1: # si domingo es el primer día del mes
			first_sunday += 1

print(first_sunday)

# [Finished in 362ms]