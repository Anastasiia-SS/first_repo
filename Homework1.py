import datetime

def get_days_from_today(date):
    today = datetime.date.today()
    delta = today - date
    return delta.days
print(get_days_from_today(datetime.date(2020, 9, 8)))