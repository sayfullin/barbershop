from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey
from database import Base

class Barbershop(Base):
    __tablename__ = 'barbershops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    description = Column(String)
    working_time = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    stars = Column(Float)
    address = Column(String)
    saloon_type = Column(String)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
       return "<Barbershop('%s')>" % (self.name)


class BarbershopUser(Base):
    __tablename__ = 'barbershop_user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    password = Column(String)
    barbershop_id = Column(Integer, ForeignKey('barbershops.id'))

    def __init__(self, barbershop_id, username, password):
        self.barbershop_id = barbershop_id
        self.username = username
        self.password = password

    def __repr__(self):
       return "<BarbershopStaff('%s')>" % (self.username)


class HaircutType(Base):
    __tablename__= 'haircut_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    barbershop_id = Column(Integer, ForeignKey('barbershops.id'))
    time_in_minutes = Column(Integer)

    def __init__(self, barbershop_id, name, price):
        self.barbershop_id = barbershop_id
        self.name = name
        self.price = price

    def __repr__(self):
       return "<BarbershopPhoto('%s')>" % (self.file_path)


class BarbershopPhoto(Base):
    __tablename__= 'barbershop_photos'

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    barbershop_id = Column(Integer, ForeignKey('barbershops.id'))

    def __init__(self, barbershop_id, file_path):
        self.barbershop_id = barbershop_id
        self.file_path = file_path

    def __repr__(self):
       return "<BarbershopPhoto('%s')>" % (self.file_path)


class Booking(Base):
    __tablename__= 'booking'
    id = Column(Integer, primary_key=True)
    barbershop_id = Column(Integer, ForeignKey('barbershops.id'))
    time_to = Column(DateTime)
    created_at = Column(DateTime)
    client_name = Column(String)
