from scripts.generator.customer import generate_fake_customers
from scripts.generator.promo import generate_fake_promos

if __name__ == "__main__":
    customers = generate_fake_customers()
    for c in customers:
        print(c)

    promos = generate_fake_promos()
    for p in promos:
        print(p)
