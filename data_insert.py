import pandas as pd
import os

from sql_model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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
Sessoion = sessionmaker(bind=engine)
session = Sessoion()
Base = declarative_base()


data_dir = ['facility.csv', 'region.csv', 'info.csv']

for file_path in data_dir:
    data = pd.read_csv('./data/{}'.format(file_path), keep_default_na=False, encoding="cp949")
    if file_path == 'info.csv':
        for index in range(len(data)):
            row = Information(
                region_id=data.loc[index][0],
                facilities_id = data.loc[index][1],
                category = data.loc[index][2],
                name = data.loc[index][3],
                tel = data.loc[index][4],
                fare = data.loc[index][5],
                latitude = data.loc[index][6],
                longitude = data.loc[index][7]
            )
            session.add(row)
            session.commit()
            print("{} DB CREATE".format(file_path))

    elif file_path == 'facility.csv':
        for index in range(len(data)):
            row = Facility(
                id=data.loc[index][0],
                name=data.loc[index][1]
            )
            session.add(row)
            session.commit()
            print("{} DB CREATE".format(file_path))

    else:
        for index in range(len(data)):
            row = Region(
                id=data.loc[index][0],
                name=data.loc[index][1]
            )

            session.add(row)
            session.commit()
            print("{} DB CREATE".format(file_path))

session.close()