import datetime
import random


def generate_random_date():
    start_date = datetime.date(2009, 2, 9)
    end_date = datetime.date(2020, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def generate_fake_services():
    services = []
    service_name = [
        'Pembelian',
        'Top-Up',
        'Tagihan',
        'Travel',
        'Entertainment',
        'Keuangan',
        'Halal Corner',
        'Tukar Tambah',
        'Tokopedia Clean',
        'Tokopedia Print',
        'Pasang Internet',
        'Langsung Laku',
        'Bayar di Tempat'
    ]

    for serv in range(len(service_name)):
        name = service_name[serv]
        
        tanggal = generate_random_date()
        date = str(tanggal.year)+'-'+str(tanggal.month)+'-'+str(tanggal.day)
    
        service = {
            'name' : name,
            'date' : date
        }

        services.append(service)
    return services