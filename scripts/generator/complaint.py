import random
from datetime import datetime


def find_duration_in_minute(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H")
    return int((d2 - d1).total_seconds() // 60)


def generate_fake_complaints(products, transactions, customers, sellers, times):
    complaints = []
    NUMBER_OF_GENERATED_COMPLAINTS = 300
    complaint_reason_composition = {
        "delay": 15,
        "order_incomplete": 8,
        "order_broken": 30,
        "order_not_match": 47
    }

    for reason in complaint_reason_composition.keys():
        num_generated_complaint = complaint_reason_composition[reason] * NUMBER_OF_GENERATED_COMPLAINTS // 100
        for _ in range(num_generated_complaint):
            product_id = random.randint(1, len(products))
            transaction_id = random.randint(1, len(transactions))
            seller_id = random.randint(1, len(sellers))
            customer_id = random.randint(1, len(customers))

            time_of_customer_complaint_id = random.randint(1, len(times))
            time_of_reconcile_id = time_of_customer_complaint_id + random.randint(1, 100)
            if time_of_reconcile_id > len(times):
                time_of_reconcile_id = len(times)

            complaint_duration = find_duration_in_minute(
                times[time_of_customer_complaint_id-1]["date"] + " " + str(times[time_of_customer_complaint_id-1]["hour"]),
                times[time_of_reconcile_id-1]["date"] + " " + str(times[time_of_reconcile_id - 1]["hour"]),
            )
            is_order_delayed = False
            is_order_incomplete = False
            is_order_broken = False
            is_order_not_match = False
            if reason == 'delay':
                is_order_delayed = True
            elif reason == 'order_incomplete':
                is_order_incomplete = True
            elif reason == 'order_broken':
                is_order_broken = True
            elif reason == 'order_not_match':
                is_order_not_match = True

            complaint = {
                'customer_id': customer_id,
                'transaction_id': transaction_id,
                'time_of_customer_complaint': time_of_customer_complaint_id,
                'product_id': product_id,
                'seller_id': seller_id,
                'time_of_reconcile': time_of_reconcile_id,
                'complaint_duration': complaint_duration,
                'is_order_delayed': is_order_delayed,
                'is_order_incomplete': is_order_incomplete,
                'is_order_broken': is_order_broken,
                'is_order_not_match': is_order_not_match
            }
            complaints.append(complaint)

    return complaints
