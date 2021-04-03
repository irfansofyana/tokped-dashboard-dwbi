# date, minute, hour, day_name, month, year, holiday_status, weekend_status, weekday_status
import datetime
import random


def generate_fake_times():
    def is_weekend(name_of_day):
        weekend_days = ['saturday', 'sunday']

        return name_of_day.lower() in weekend_days

    dates = []

    date_iterator = datetime.date(2017, 1, 1)
    while date_iterator != datetime.date.today():
        day_name = date_iterator.strftime("%A")
        month = date_iterator.month
        year = date_iterator.year

        for hour in range(11, 22):
            date = {
                'date': str(date_iterator),
                'hour': hour,
                'minute': 0,
                'day_name': day_name,
                'month': month,
                'year': year,
            }

            dates.append(date)

        date_iterator = date_iterator + datetime.timedelta(days=1)

    return dates