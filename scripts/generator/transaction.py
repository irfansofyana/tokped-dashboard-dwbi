import random


def generate_fake_transactions(customers, products, promos, times, services, sellers):
    transactions = []
    NUMBER_OF_GENERATED_TRANSACTIONS = 100000
    cnt_success = 95 * NUMBER_OF_GENERATED_TRANSACTIONS // 100

    for i in range(NUMBER_OF_GENERATED_TRANSACTIONS):
        product_id = random.randint(1, len(products))
        customer_id = random.randint(1, len(customers))
        time_id = random.randint(1, len(times))
        service_id = random.randint(1, len(services))
        promo_id = random.randint(1, len(promos))
        seller_id = random.randint(1, len(sellers))
        transaction_status = 'Success' if i < cnt_success else 'Fail'

        product_price = products[product_id-1]["product_price"]
        promo_discount = promos[promo_id-1]["promo_discount"] * product_price // 100
        total_price = product_price - promo_discount
        if transaction_status == 'Fail':
            total_price = None

        transaction = {
            'customer_id': customer_id,
            'seller_id': seller_id,
            'service_id': service_id,
            'time_id': time_id,
            'product_id': product_id,
            'promo_id': promo_id,
            'transaction_status': transaction_status,
            'total_price': total_price
        }
        transactions.append(transaction)

    return transactions
