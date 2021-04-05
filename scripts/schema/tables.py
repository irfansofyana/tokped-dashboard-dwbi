from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__="Customer"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    customer_age = Column(Integer, nullable=False)
    customer_location = Column(String(100), nullable=False)
    customer_gender = Column(String(10), nullable=False)
    customer_dropPoint = Column(String(100), nullable=False)
    customer_phoneNumber = Column(String(20), nullable=False)
    customer_email = Column(String(50), nullable=False)

    def __init__(self, customer):
        self.customer_age = customer["customer_age"]
        self.customer_location = customer["customer_location"]
        self.customer_gender = customer["customer_gender"]
        self.customer_dropPoint = customer["customer_dropPoint"]
        self.customer_phoneNumber = customer["customer_phoneNumber"]
        self.customer_email = customer["customer_email"]


class Promo(Base):
    __tablename__="Promo"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    promo_name = Column(String(100), nullable=False)
    promo_discount = Column(Integer, nullable=False)
    promo_category = Column(String(100), nullable=False)

    def __init__(self, promo):
        self.promo_name = promo["promo_name"]
        self.promo_discount = promo["promo_discount"]
        self.promo_category = promo["promo_category"]


class Time(Base):
    __tablename__ = "Time"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    date = Column(Date, nullable=False)
    day_name = Column(String(20), nullable=False)
    hour = Column(Integer)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    def __init__(self, time):
        self.date = time["date"]
        self.day_name = time["day_name"]
        self.hour = time["hour"]
        self.month = time["month"]
        self.year = time["year"]


class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_category = Column(String(100), nullable=False)
    product_price = Column(Integer, nullable=False)
    product_weight = Column(Integer)

    def __init__(self, product):
        self.product_name = product["product_name"]
        self.product_price = product["product_price"]
        self.product_category = product["product_category"]
        self.product_weight = product["product_weight"]

class ClickRate(Base):
    __tablename__ = "ClickRate"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    product_id = Column(Integer, ForeignKey('Product.id'))
    start_time_id = Column(Integer, ForeignKey('Time.id'))
    end_time_id = Column(Integer, ForeignKey('Time.id'))
    number_of_clicks = Column(Integer, nullable=False)
    duration_in_minute = Column(Integer, nullable=False)
    click_rate = Column(Integer, nullable=False)

    def __init__(self, click_rate):
        self.product_id = click_rate["product_id"]
        self.start_time_id = click_rate["start_time_id"]
        self.end_time_id = click_rate["end_time_id"]
        self.number_of_clicks = click_rate["number_of_clicks"]
        self.duration_in_minute = click_rate["duration_in_minute"]
        self.click_rate = click_rate["click_rate"]


class Service(Base):
    __tablename__ = "Service"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    service_name = Column(String(100), nullable=False)
    service_birth = Column(Date, nullable=False)

    def __init__(self, service):
        self.service_name = service["name"]
        self.service_birth = service["date"]