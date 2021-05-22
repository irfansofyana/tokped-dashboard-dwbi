from faker import Faker


def generate_fake_sellers():
    sellers = []
    NUMBER_OF_GENERATED_SELLERS = 500

    faker = Faker('id_ID')
    fake = faker['id_ID']

    for _ in range(NUMBER_OF_GENERATED_SELLERS):
        seller_name = fake.company()
        seller_location = fake.city()
        seller_address = fake.address()
        seller_contact_person = fake.phone_number()
        seller_email = seller_name + fake.domain_name()

        seller = {
            'seller_name': seller_name,
            'seller_location': seller_location,
            'seller_address': seller_address,
            'seller_contact_person': seller_contact_person,
            'seller_email': seller_email
        }

        sellers.append(seller)

    return sellers
