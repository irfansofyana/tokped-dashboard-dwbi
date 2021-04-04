# date, minute, hour, day_name, month, year, holiday_status, weekend_status, weekday_status
import datetime
import random


def generate_fake_times():
    dates = []

    date_iterator = datetime.date(2017, 1, 1)
    while date_iterator != datetime.date.today():
        day_name = date_iterator.strftime("%A")
        month = date_iterator.month
        year = date_iterator.year

        for hour in range(0, 23):
            date = {
                'date': str(date_iterator),
                'day_name': day_name,
                'hour': hour,
                'minute': 0,
                'month': month,
                'year': year,
            }

            dates.append(date)

        date_iterator = date_iterator + datetime.timedelta(days=1)

    return dates