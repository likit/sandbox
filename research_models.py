from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, Date, ForeignKey, Float, Boolean)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///research.db')


# Change att duration and funding_contract
class FundingSource(Base):
    __tablename__ = 'funding_sources'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    source = Column('source', String())


class FundingAgency(Base):
    __tablename__ = 'funding_agencies'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String())


class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column('staff_id', Integer, autoincrement=True, primary_key=True)
    staff_firstname = Column('staff_firstname', String())
    staff_lastname = Column('staff_lastname', String())
    staff_email = Column('staff_email', String())


class Department(Base):
    __tablename__ = 'department'
    department_id = Column('department_id', Integer, autoincrement=True, primary_key=True)
    department_name = Column('department_name', String())


class ResearchProject(Base):
    __tablename__ = 'research_projects'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    title_th = Column('title_th', String())
    title_en = Column('title_en', String())
    est_funding = Column('est_funding',Float())
    startdate = Column('startdate', Date())
    enddate = Column('enddate', Date())
    contract = Column('contract', Boolean())


class Date(Base):
    __tablename__ = 'date'
    date_id = Column('date_id', Integer, autoincrement=True, primary_key=True)
    date = Column('date', Date())
    calendar_month = Column('calendar_month', String(3))
    calendar_year = Column('calendar_year', Integer())
    fiscal_year_month = Column('fiscal_year_month', String(8))
    fiscal_quarter = Column('fiscal_quarter', String(2))
    academic_year = Column('academic_year', Integer())


'''
class FundingResearchFact(Base):
    __tablename__ = 'funding_research_fact'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    funding_id = Column('funding_id', ForeignKey('funding_sources.id'))
    research_id = Column('research_id', ForeignKey('research.research_id'))
    staff_id = Column('staff_id', ForeignKey('staff.staff_id'))
    department_id = Column('department_id', ForeignKey('department.department_id'))
    date_id = Column('date_id', ForeignKey('date.date_id'))
    each_funding = Column('total_funding', Float())
'''


if __name__ == '__main__':
    Base.metadata.create_all(engine)
