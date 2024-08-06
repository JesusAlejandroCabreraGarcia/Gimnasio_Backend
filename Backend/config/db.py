from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3307/test'  #Conexión local
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://avnadmin:AVNS_WWwmfvuplg6Muz-kyNC@mysql-20401d83-alejandroxlllc-f203.e.aivencloud.com:28124/defaultdb'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
