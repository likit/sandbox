from sqlalchemy import (create_engine, Table, Column, Integer,
                        Numeric, String, Boolean, Date, ForeignKey, Float)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




engine = create_engine('sqlite:///research.db')



#Change att duration and funding_contract
class FundingSource(Base):
    __tablename__ = 'funding_sources'
    funding_id = Column('funding_id', Integer, autoincrement=True, primary_key=True)
    funding_source = Column ('funding_source',String())
    funding_agency = Column ('funding_agency',String())




class  ResearchwithFund(Base):
    __tablename__ = 'researchwithfund'
    research_id = Column('research_id', Integer, autoincrement=True, primary_key=True)
    research_name_th = Column ('research_name_th',String())
    research_name_en = Column ('research_name_en',String())
    research_field = Column ('research_field',String())
    research_budget_thisyear  = Column('research_budget_thisyear', Integer())
    research_budget_throughtout = Column('research_budget_throughtout', Integer())
    research_startdate = Column('research_startdate', Date())
    research_enddate = Column('research_enddate', Date())
    duration = Column('duration', Boolean())
    funding_contract = Column('funding_contract', Boolean())


class  Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column('staff_id', Integer, autoincrement=True, primary_key=True)
    staff_firstname = Column ('staff_firstname',String())
    staff_lastname = Column ('staff_lastname',String())
    staff_email = Column ('staff_email',String())
    department_name = Column ('department_name',String())

class  Date(Base):
    __tablename__ = 'date'
    date_id = Column('date_id', Integer, autoincrement=True, primary_key=True)
    date = Column('date', Date())
    calendar_month = Column('calendar_month', String(3))
    calendar_year = Column('calendar_year', Integer())
    fiscal_year_month = Column('fiscal_year_month', String(8))
    fiscal_quarter = Column('fiscal_quarter', String(2))
    academic_year = Column('academic_year', Integer())

class FundingResearchFact(Base):
    __tablename__ = 'funding_research_fact'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    funding_id = Column('funding_id',  ForeignKey('funding_sources.funding_id'))
    research_id = Column('research_id',  ForeignKey('researchwithfund.research_id'))
    staff_id = Column('staff_id',  ForeignKey('staff.staff_id'))
    date_id = Column('date_id',  ForeignKey('date.date_id'))
    totalfunding = Column('totalfunding', Integer())
    totalstaff = Column('totalstaff', Integer())
    totalcontractproject = Column('totalcontractproject', Integer())
    fundingperperson = Column('fundingperperson', Float())
    fundingperdepartment = Column('fundingperdepartment', Float())

Base.metadata.create_all(engine)