from scripts.generator.customer import generate_fake_customers

if __name__ == "__main__":
    customers = generate_fake_customers()
    for c in customers:
        print(c)
