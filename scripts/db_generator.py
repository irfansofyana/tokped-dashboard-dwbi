from scripts.schema.tables import *
from scripts.generator.customer import *
from scripts.generator.time import *
from scripts.generator.promo import *
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
            generate_fake_times: Time
        }

        for generator in generator_and_table:
            table = generator_and_table[generator]
            fake_data = generator()
            load_table(session, table, fake_data)

    except Exception as err:
        print(err)
