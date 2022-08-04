import json
from datetime import datetime
import psycopg2
from flask import Flask, request
from flask import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()

class sasidharCompany(Base):
    __tablename__ = "sasidhar_company"
    Name = Column("name", String)
    Age = Column("age", Integer)
    Emailid = Column("emailid", String)
    Address = Column("address", String)
    Salary = Column("salary", Integer)
    Mobile = Column("mobile", Integer, primary_key=True)
    Is_paid_pfo = Column("is_paid_pfo", String)