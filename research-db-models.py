from sqlalchemy import (create_engine, Table, Column, Integer,
                        Numeric, String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FundingSource(Base):
    __tablename__ = 'funding_sources'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    agency = Column('agency', String())


engine = create_engine('sqlite:///research.db')

Base.metadata.create_all(engine)


