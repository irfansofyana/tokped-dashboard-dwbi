from datetime import datetime
import random


def find_duration_in_minute(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H")
    return int((d2 - d1).total_seconds() // 60)


def generate_fake_click_rates(products, times):
    click_rates = []
    NUMBER_OF_GENERATED_CLICK_RATES = 5000

    for _ in range(NUMBER_OF_GENERATED_CLICK_RATES):
        product_id = random.randint(1, len(products))
        start_tid = random.randint(1, len(times) - 24)
        end_tid = start_tid + random.randint(1, 24)
        duration_in_minute = find_duration_in_minute(
            times[start_tid]["date"] + " " + str(times[start_tid]["hour"]),
            times[end_tid]["date"] + " " + str(times[end_tid]["hour"])
        )
        number_of_clicks = random.randint(1, 10000)
        click_rate = number_of_clicks // duration_in_minute

        click_rate_obj = {
            'product_id': product_id,
            'start_time_id': start_tid,
            'end_time_id': end_tid,
            'number_of_clicks': number_of_clicks,
            'duration_in_minute': duration_in_minute,
            'click_rate': click_rate
        }
        click_rates.append(click_rate_obj)

    return click_rates
