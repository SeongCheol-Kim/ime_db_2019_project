import os
import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


ROOT_DIR = os.getcwd()
SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')
secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

Base = declarative_base()


def connect_database():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
        secrets['RDS_USER_ID'],
        secrets['RDS_USER_PASSWORD'],
        secrets['RDS_USER_URL'],
        secrets['RDS_PORT'],
        secrets['DATABASE_NAME']
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    return session