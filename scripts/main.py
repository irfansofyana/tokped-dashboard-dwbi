from scripts.schema.tables import *
from scripts.generator.customer import *
from scripts.generator.time import *
from scripts.generator.promo import *
from scripts.generator.product import *
from scripts.generator.click_rate import *
from scripts.generator.service import *
from scripts.generator.transaction import *
from scripts.generator.seller import *
from scripts.generator.complaint import *
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
        print('Error Create MySQL Engine: ', err)


def create_session(engine):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as err:
        print('Error Create Session: ', err)


def generate_and_load_dimension_tables(session):
    try:
        generator_and_table = {
            generate_fake_promos: Promo,
            generate_fake_customers: Customer,
            generate_fake_times: Time,
            generate_fake_products: Product,
            generate_fake_services: Service,
            generate_fake_sellers: Seller,
        }
        tables_name = ["Promo", "Customer", "Time", "Product", "Service", "Seller"]
        generated_fake_data = {}

        for i, generator in enumerate(generator_and_table):
            table_class = generator_and_table[generator]

            generated_fake_data[tables_name[i]] = generator()

            load_table(
                session,
                table_class,
                generated_fake_data[tables_name[i]]
            )

            print(f"Generate {tables_name[i]} table success!")

        return generated_fake_data
    except Exception as err:
        print("ERROR Generate and Load Dimension tables: ", err)


def generate_and_load_transaction_table(session, customer, product, promo, time, service, seller):
    try:
        fake_transactions = generate_fake_transactions(
            customer,
            product,
            promo,
            time,
            service,
            seller
        )
        load_table(session, Transaction, fake_transactions)
        print("Generate and Load Transaction table success!")
        return fake_transactions
    except Exception as err:
        print("ERROR Generate and Load Transaction table: ", err)


def generate_and_load_complaint_table(session, product, transaction, customer, seller, time):
    try:
        fake_complaints = generate_fake_complaints(
            product,
            transaction,
            customer,
            seller,
            time
        )
        load_table(session, Complaint, fake_complaints)
        print("Generate and Load Complaint table success!")
    except Exception as err:
        print("ERROR Generate and Load Complaint table: ", err)


def generate_and_load_click_rates_table(session, product, time):
    try:
        fake_click_rates = generate_fake_click_rates(product, time)
        load_table(session, ClickRate, fake_click_rates)
        print("Generate ClickRate table success!")
    except Exception as err:
        print("ERROR Generate and Load Click Rate table", err)


def generate_and_load_fact_tables(session, dimension_tables):
    try:
        generate_and_load_click_rates_table(
            session,
            dimension_tables["Product"],
            dimension_tables["Time"]
        )
        dimension_tables["Transaction"] = generate_and_load_transaction_table(
            session,
            dimension_tables["Customer"],
            dimension_tables["Product"],
            dimension_tables["Promo"],
            dimension_tables["Time"],
            dimension_tables["Service"],
            dimension_tables["Seller"]
        )
        generate_and_load_complaint_table(
            session,
            dimension_tables["Product"],
            dimension_tables["Transaction"],
            dimension_tables["Customer"],
            dimension_tables["Seller"],
            dimension_tables["Time"]
        )
    except Exception as err:
        print("ERROR Generate and Loading fact tables: ", err)


if __name__ == "__main__":
    mysql_engine = create_mysql_engine(MYSQL_CONNECTION_STRING)
    session = create_session(mysql_engine)

    Base.metadata.create_all(mysql_engine)

    try:
        dimension_tables = generate_and_load_dimension_tables(session)
        generate_and_load_fact_tables(session, dimension_tables)
    except Exception as err:
        print("ERROR in generating fake data: ", err)
