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


def fill_product_category_specific(products):
    pc_specific_candidates = {
        "Buku": ["Buku Sidu", "Buku Kiki", "Buku Harvest"],
        "Dapur": ["Kompor Astra", "Panci Happy Call", "Magic jar Panasonic"],
        "Elektronik": [
            "Earphone Joyseus",
            "Sony SRS - ultra sound",
            "Kipas Angin Dinding Cosmos",
        ],
        "Fashion Anak & Bayi": [
            "Jam Tangan Karakter",
            "Kostum Putri Duyung Anak",
            "Sepatu Bayi Elmo"
        ],
        "Fashion Muslim": [
            "Sarung Gajah Duduk",
            "Sarung Wadimor",
            "Kerudung Rabbani"
        ],
        "Fashion Pria": [
            "Erigo Jogger Pants",
            "Brodo Sneakers",
            "Kalibre Waist Bag"
        ],
        "Fashion Wanita": [
            "Cotton On Mini Dress",
            "Yoenik Apparel Ulvaru Hoodie",
            "Marks & Spencer Blouse"
        ],
        "Film & Musik": [
            "Gitar Yamaha",
            "Biola Yamaha",
            "DVD Spiderman 3",
            "Keyboard Yamaha",
        ],
        "Gaming": [
            "Mouse Asus Gaming",
            "Keyboard Mekanik",
            "Keyboard RGB",
        ],
        "Handphone & Tablet": [
            "Handphone Xiaomi",
            "Handphone Samsung",
            "Ipad",
            "Iphone",
        ],
        "Ibu & Bayi": [
            "Sweety Popok Silver Pants XXL 3x24s",
            "Nepia Genki Pants L 30",
            "Caplang Minyak Kayu Putih 210ml",
            "Sun Bubur Bayi 120G",
            "Selimut Bayi 76x102",
        ],
        "Kamera": [
            "Sony DSLR",
            "Canon Mirrorless",
            "Nikon DSLR",
            "Xiaomi Action Cam",
            "GoPro"
        ],
        "Kecantikan": [
            "Garnier Super UV Light Complete Sunscreen",
            "Erha Truwhite Brightening Facial Wash",
            "Cetaphil Gentle Skin Cleanser",
            "Garnier Micellar Water Pink"
        ],
        "Kesehatan": [
            "Masker Medis 3ply",
            "Madu Zestmag",
            "Forumen Ear Drops",
            "Obat pelangsing badan",
            "Sangobion",
        ],
        "Komputer & Laptop": [
            "Asus ROG Zephyrus M15",
            "HP Pavilion Gaming",
            "Acer Nitro 5",
            "Asus Swift 3",
            "Asus Vivobook 14"
        ],
        "Logam Mulia": [
            "Logam Mulia Antam 10gram",
            "USB Logam Mulia 0,1gram",
            "Lotus Archi 1 gram CertiEye",
            "Logam Mulia Antam 15 gram"
        ],
        "Mainan & Hobi": [
            "Model Gundam",
            "Kartu YugiOh",
            "Set Kartu Remi",
            "Play Doh Mini",
            "Hotwheals",
        ],
        "Makanan & Minuman": [
            "Indomie",
            "Coca Cola",
            "Aqua",
            "Supermie",
            "Natadecoco"
        ],
        "Office & Stationery": [
            "Pulpen Snowman",
            "Pensil Faber Castell",
            "Pulpen Standard",
            "Pulpen Standard",
            "Pulpen Pilot"
        ],
        "Olahraga": [
            "Bola bisbol",
            "Tongkat bisbol",
            "Bola golf",
            "Bola basket",
        ],
        "Otomotif": [
            "Durable Karpet Karet PVC",
            "Cover Mobil Durable",
            "Anti Fog Helm Film",
            "Busi iridium",
            "Bohlam Headlamp"
        ],
        "Perawatan Hewan": [
            "Whiskas Dry 1, 2 kg",
            "Slow Feeder",
            "Mainan Tali Gigitan Anjing",
            "Me - O seafood 1 Kg"
        ],
        "Perawatan Tubuh": [
            "Pepsodent Sikat Gigi",
            "Dettol Cairan Antiseptik"
        ],
        "Perlengkapan Pesta & Craft": [
            "Lilin putih",
            "Lilin angka",
            "Topi ulang tahun",
        ],
        "Pertukangan": [
            "Kloset Toto",
            "Kuas Cat Kayu",
            "Kran Air Stainless"
        ],
        "Properti": [
            "Meja lipat",
            "Meja standa",
            "Kursi polygon"
        ],
        "Rumah Tangga": [
            "Meja Belajar Anak",
            "Lemari Pakaian 2 Pintu",
            "Meja TV Kayu"
        ],
        "Tour & Travel": [
            "Pop! Hotel Voucher",
            "Paket Tour Bromo",
            "Voucher Langganan Cititrans",
        ],
        "Wedding": [
            "Paket Prewedding Indoor",
            "Cincin Couple Emas",
            "Kotak Hantaran Seserahan"
        ],
    }

    for product in products:
        category = product['product_category']
        if category in pc_specific_candidates:
            pc_specific_candidate = pc_specific_candidates[category]
            chosen = random.randint(0, len(pc_specific_candidate) - 1)
            product['product_category_specific'] = pc_specific_candidate[chosen]
        else:
            product['product_category_specific'] = category

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

    products = fill_product_category_specific(products)

    return products
