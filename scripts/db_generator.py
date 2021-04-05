from scripts.schema.tables import *
from scripts.generator.customer import *
from scripts.generator.time import *
from scripts.generator.promo import *
from scripts.generator.product import *
from scripts.generator.click_rate import *
from scripts.generator.service import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from scripts.schema.tables import Base

MYSQL_CONNECTION_STRING = "mysql+mysqldb://root:@localhost:3306/tokped_dwbi"
# format: mysql+mysqldb://<user>:<password>@<host>:<port>/<database_name>


def load_table(session, table, fake_data):
    for data in fake_data:
        row = table(data)
        session.add(row)
    session.commit()


def create_mysql_engine(mysql_connection_string):
    try:
        mysql_engine = create_engine(mysql_connection_string)
        return mysql_engine
    except Exception as err:
        print('Error: ', err)


def create_session(engine):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as err:
        print('Error: ', err)


if __name__ == "__main__":
    mysql_engine = create_mysql_engine(MYSQL_CONNECTION_STRING)
    session = create_session(mysql_engine)

    Base.metadata.create_all(mysql_engine)

    try:
        generator_and_table = {
            generate_fake_promos: Promo,
            generate_fake_customers: Customer,
            generate_fake_times: Time,
            generate_fake_products: Product,
            generate_fake_services: Service
        }
        process = ["Promo", "Customer", "Time", "Product", "Service"]
        fake_data = [None] * 5

        for i, generator in enumerate(generator_and_table):
            table = generator_and_table[generator]
            fake_data[i] = generator()
            load_table(session, table, fake_data[i])

            print(f"Generate {process[i]} table success!")

        fake_click_rates = generate_fake_click_rates(fake_data[3], fake_data[2])
        load_table(session, ClickRate, fake_click_rates)
        print(f"Generate ClickRate table success!")
    except Exception as err:
        print(err)
