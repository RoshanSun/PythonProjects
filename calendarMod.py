import calendar

# The function value signifies # of chars to return for each dow
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

# Year, Month
print(calendar.month(2019, 3))

# 2D array that consists of each week
print(calendar.monthcalendar(2019, 3))

# print all 12 months
print(calendar.calendar(2019))

dow = calendar.weekday(2019, 12, 22)
print(dow)

is_leap = calendar.isleap(2020)
print(is_leap)

# exclusive range on years - 2nd parameter not counted
num_leap_days = calendar.leapdays(2000, 3000)
print(num_leap_days)