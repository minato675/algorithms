import datetime as dt
day = dt.datetime.now()
month = day.strftime("%m")
print(f'{day.year}-{month}-{day.day}')