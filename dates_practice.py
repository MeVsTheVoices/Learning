import datetime

x = datetime.datetime(2023, 12, 15)

print(x.strftime("%B %d, %Y"))

x = datetime.datetime.now()

print(x)

x = datetime.datetime(year = 2021, day = 22, month = 6)

print(x)

x = datetime.datetime(year = 1991, day = 2, month = 12, hour = 23)

print(x)
print(x.strftime("%B %d, %Y at %I %p"))

