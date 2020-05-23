
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
engine = create_engine(
    oracle_connection_string.format(

        username="PROJECT",
        password="Oracle",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECT",

    )
    , echo=True
)

Base = declarative_base()

class Customer (Base):
    __tablename__ = 'customer'

    message = Column(String(40))
    customer_name = Column(String(10))
    age = Column(Integer)
    email = Column(String(20), primary_key=True)
    tours = relationship('Tour', secondary='user_tour')



    def __init__(self, message, customer_name, age, email):
        """"""
        self.message = message
        self.customer_name = customer_name
        self.age = age
        self.email = email


class Tour (Base):
    __tablename__ = 'tour'

    tour_name = Column(String(30),  primary_key=True)
    country = Column(String(20))
    year_category = Column(String(20))
    duration_tour = Column(Integer)
    price = Column(Integer)
    customers = relationship('Customer', secondary = 'user_tour')

class User_tour (Base):
    __tablename__= 'user_tour'
    booking_id = Column(Integer, primary_key=True)
    ttour_name = Column (String(30), ForeignKey('tour.tour_name'), primary_key= True )
    cemail = Column (String(20), ForeignKey('customer.email'), primary_key= True)

Base.metadata.create_all(engine)




