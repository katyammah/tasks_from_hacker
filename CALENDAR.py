import calendar
MM, DD, YYYY = map(int, input().split())

day = calendar.weekday(YYYY, MM, DD)
name = calendar.day_name[day]
print(name.upper())