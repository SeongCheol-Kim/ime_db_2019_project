import os
import json
from sqlalchemy import Column, String, Integer, Float, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))


engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
    secrets['LOCAL_USER_ID'],
    secrets['LOCAL_USER_PASSWORD'],
    secrets['LOCAL_USER_URL'],
    secrets['RDS_PORT'],
    secrets['DATABASE_NAME']
))
Session = sessionmaker(bind=engine)
Base = declarative_base()


info_association = Table(
    'total_information', Base.metadata,
    Column('RegionID', Integer, ForeignKey('regions.id')),
    Column('CategoryID', Integer, ForeignKey('facilities.id')),
    Column('ObjectID', Integer, ForeignKey('informations.id'))
)


class Region(Base):                                  # 지역 구분
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    code = Column(String(32))          # 지구구분코드
    name = Column(String(64))

    def __init__(self, code, name):

        self.code = code
        self.name = name


class Facility(Base):                                # 종목 구분
    __tablename__ = 'facilities'

    id = Column(Integer, primary_key=True)
    code = Column(String(32))      # 지형지물 코드
    name = Column(String(32))

    def __init__(self, code, name):
        self.code = code
        self.name = name


class Information(Base):                            # 종합 정보
    __tablename__ = 'informations'

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    facilities_id = Column(Integer, ForeignKey('facilities.id'), nullable=False)
    category = Column(String(32))
    name = Column(String(64))
    tel = Column(String(64))
    fare = Column(String(256))
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, category, name, tel, fare, latitude, longitude):
        self.category = category
        self.name = name
        self.tel = tel
        self.fare = fare
        self.latitude = latitude
        self.longitude = longitude