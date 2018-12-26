import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from research_models import *
from pandas import read_excel

engine = create_engine('sqlite:///research.db')
Session = sessionmaker(bind=engine)
session = Session()

#--------------FundingSource-------------------
fund_df = read_excel('samplefunding.xlsx', sheet_name='info')
for ix,row in fund_df.iterrows():
    funding_sources = FundingSource(
        funding_source = row['all funding source'],
        funding_agency = row['all funding agency']
    )
    session.add(funding_sources)
session.commit()
#--------------Staff---------------------------
staff_df = read_excel('samplefunding.xlsx', sheet_name='info')
for ix,row in staff_df.iterrows():
    staff = Staff(
        staff_firstname=row['first name'],
        staff_lastname=row['last name'],
        staff_email=row['all main researcher email'],
    )
    session.add(staff)
session.commit()
#--------------Department----------------------
department_df = read_excel('samplefunding.xlsx', sheet_name='info')
for ix,row in department_df.iterrows():
    department = Department(
        department_name=row['all department']
    )
    session.add(department)
session.commit()
#--------------Research------------------------
research_df = read_excel('samplefunding.xlsx',sheet_name='funding')
for ix,row in research_df.iterrows():
    research = Research_df(
        research_title_th = row['research title thai'],
        research_title_en = row['research title eng'],
       # research_field = row['research_field'],
       # research_budget_thisyear = row['research_budget_thisyear'],
        est_funding = row['amount fund'],
        research_startdate = int(datetime.strftime(row['start date'], '%m%d%Y')),
        research_enddate = int(datetime.strftime(row['end date'], '%m%d%Y')),
      # duration = row['duration'],
        research_contract = row['research contract']
    )
    session.add(research)
session.commit()


#st = session.query(Staff).filter(Staff.staff_email=='napat.son').first()
#st = session.query(Staff).filter(Staff.staff_email==row['staff_email']).first()
#st.staff_id

#int(datetime.strftime(row['research_startdate'], '%Y%m%d'))


