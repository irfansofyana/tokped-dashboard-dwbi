from scripts.generator.customer import generate_fake_customers
from scripts.generator.promo import generate_fake_promos
from scripts.generator.time import generate_fake_times
from scripts.generator.product import generate_fake_products
from scripts.generator.click_rate import generate_fake_click_rates

if __name__ == "__main__":
    customers = generate_fake_customers()
    for c in customers:
        print(c)

    promos = generate_fake_promos()
    for p in promos:
        print(p)

    times = generate_fake_times()
    for t in times:
        print(t)

    products = generate_fake_products()
    for p in products:
        print(p)

    cr = generate_fake_click_rates(products, times)
    for c in cr:
        print(c)