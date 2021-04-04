from faker import Faker
import random


def generate_age(youngest, oldest):
    return random.randint(youngest, oldest)


def generate_fake_customers():
    customers = []
    NUMBER_OF_GENERATED_CUSTOMERS = 1000

    faker = Faker('id_ID')
    fake = faker['id_ID']

    age_composition = {
        (15, 35): 50,
        (31, 40): 30,
        (41, 50): 15,
        (51, 70): 5
    }

    for range_age in age_composition:
        for _ in range(age_composition[range_age] * NUMBER_OF_GENERATED_CUSTOMERS // 100):
            age = generate_age(range_age[0], range_age[1])
            gender = 'pria' if random.randint(0, 1) else 'wanita'
            name = fake.name_male() if gender == 'pria' else fake.name_female()
            location = fake.city()
            address = fake.address()
            drop_point = fake.street_address()
            phone_number = fake.phone_number()

            customer = {
                'customer_age': age,
                'customer_location': location,
                'customer_gender': gender,
                'customer_address': address,
                'customer_dropPoint': drop_point,
                'customer_phoneNumber': phone_number,
                'customer_email': name + fake.domain_name()
            }

            customers.append(customer)

    return customers
