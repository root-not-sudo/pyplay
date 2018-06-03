from datetime import date


d0 = date(1983, 11, 3)
d1 = date.today()
dayssold = d1 - d0
print("today Brent is {0:.1f}".format(dayssold.days/365.25), "years old")
