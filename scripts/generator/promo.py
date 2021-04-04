from faker import Faker
import random


def generate_fake_promos():
    promos = []
    NUMBER_OF_GENERATED_PROMOS = 100
    faker = Faker('id_ID')
    fake = faker['id_ID']

    categories_composition = {
        'Promo 1': 40,
        'Promo 2': 30,
        'Promo 3': 15,
        'Promo 4': 10,
        'Promo 5': 5
    }
    discount_range_composition = [
        (5, 15, 35),
        (16, 55, 30),
        (56, 75, 20),
        (76, 80, 10),
        (81, 99, 5),
    ]
    discount_iterator = 0
    discount_counter = 0

    for category in categories_composition:
        promo_category = category
        composition = categories_composition[category] * NUMBER_OF_GENERATED_PROMOS // 100

        for _ in range(composition):
            promo_name = "Promo " + fake.first_name_nonbinary()
            lowest_val_discount = discount_range_composition[discount_iterator][0]
            highest_val_discount = discount_range_composition[discount_iterator][1]
            promo_discount = random.randint(lowest_val_discount, highest_val_discount)

            discount_counter += 1
            if discount_counter == discount_range_composition[discount_iterator][2]:
                discount_counter = 0
                discount_iterator += 1

            promo = {
                'promo_name': promo_name,
                'promo_discount': promo_discount,
                'promo_category': promo_category
            }
            promos.append(promo)

    return promos
