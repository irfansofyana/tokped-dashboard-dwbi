import random
from faker import Faker


def random_number(r):
    return random.randint(r[0], r[1])


def generate_product_belanja(fake):
    products = []
    category_type_and_freq = {
        "Buku": random_number((10, 20)),
        "Dapur": random_number((21, 50)),
        "Elektronik": random_number((200, 500)),
        "Fashion Anak & Bayi": random_number((51, 100)),
        "Fashion Muslim": random_number((51, 100)),
        "Fashion Pria": random_number((51, 100)),
        "Fashion Wanita": random_number((51, 100)),
        "Film & Musik": random_number((51, 100)),
        "Gaming": random_number((21, 50)),
        "Handphone & Tablet": random_number((21, 50)),
        "Ibu & Bayi": random_number((10, 20)),
        "Kamera": random_number((10, 20)),
        "Kecantikan": random_number((10, 20)),
        "Kesehatan": random_number((10, 20)),
        "Komputer & Laptop": random_number((21, 50)),
        "Logam Mulia": random_number((10, 20)),
        "Mainan & Hobi": random_number((10, 20)),
        "Makanan & Minuman": random_number((200, 500)),
        "Office & Stationery": random_number((21, 50)),
        "Olahraga": random_number((21, 50)),
        "Otomotif": random_number((10, 20)),
        "Perawatan Hewan": random_number((10, 20)),
        "Perawatan Tubuh": random_number((10, 20)),
        "Perlengkapan Pesta & Craft": random_number((10, 20)),
        "Pertukangan": random_number((21, 50)),
        "Properti": random_number((10, 20)),
        "Rumah Tangga": random_number((21, 50)),
        "Tour & Travel": random_number((10, 20)),
        "Wedding": random_number((10, 20)),
    }

    for category in category_type_and_freq:
        for _ in range(category_type_and_freq[category]):
            name = "product " + fake.first_name_nonbinary()
            price = random.randint(1, 1000) * 1000
            weight = random.randint(1, 10)

            product = {
                'product_name': name,
                'product_category': category,
                'product_price': price,
                'product_weight': weight,
            }

            products.append(product)
    return products


def generate_product_investasi(fake):
    products = []

    investasi = [
        "Apply Kartu Kredit",
        "Asuransi",
        "Asuransi Perjalanan",
        "BRI Ceria",
        "Dana Impian"
    ]

    for category in investasi:
        for _ in range(10):
            name = "product " + fake.first_name_nonbinary()
            price = random.randint(1, 5000) * 1000
            product = {
                'product_name': name,
                'product_category': category,
                'product_price': price,
                'product_weight': None,
            }
            products.append(product)

    return products


def generate_product_pajak(fake):
    products = []
    pajak = [
        "E - Samsat",
        "Pajak PBB",
        "Penerimaan Negara",
        "Retribusi",
    ]
    for category in pajak:
        name = "product " + fake.first_name_nonbinary()
        price = random.randint(100, 3000) * 1000
        product = {
            'product_name': name,
            'product_category': category,
            'product_price': price,
            'product_weight': None,
        }
        products.append(product)
    return products


def generate_product_pendidikan(fake):
    products = []
    pendidikan = [
        "Belajar",
        "Kartu Prakerja",
        "Review Kartu Prakerja",
    ]
    for category in pendidikan:
        for _ in range(20):
            name = "product " + fake.first_name_nonbinary()
            price = random.randint(100, 1000) * 1000
            product = {
                'product_name': name,
                'product_category': category,
                'product_price': price,
                'product_weight': None,
            }
            products.append(product)
    return products


def generate_product_topup(fake):
    products = []
    topup = [
        "token listrik",
        "pulsa",
        "emoney"
    ]
    for category in topup:
        for _ in range(30):
            name = "product " + fake.first_name_nonbinary()
            price = random.randint(50, 2000) * 1000
            product = {
                'product_name': name,
                'product_category': category,
                'product_price': price,
                'product_weight': None,
            }
            products.append(product)
    return products


def generate_fake_products():
    products = []
    faker = Faker('id_ID')
    fake = faker['id_ID']

    products += generate_product_belanja(fake)
    products += generate_product_investasi(fake)
    products += generate_product_pajak(fake)
    products += generate_product_topup(fake)
    products += generate_product_pendidikan(fake)

    return products
