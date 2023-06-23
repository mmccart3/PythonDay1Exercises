import datetime

todays_date = datetime.date.today()

my_birth_date = datetime.date(1965,4,29)

print (todays_date)
print (my_birth_date)

days_since_born = todays_date - my_birth_date

print(days_since_born)