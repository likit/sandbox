from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from research_models import *
from pandas import read_excel

engine = create_engine('sqlite:///research.db')
Session = sessionmaker(bind=engine)
session = Session()

#--------------FundingSource-------------------
info_df = read_excel('samplefunding.xlsx', sheet_name='info')

for ix,row in info_df.iterrows():
    funding_sources = FundingSource(
        funding_source = row['all funding source'],
        funding_agency = row['all funding agency']
    )
    staff = Staff(
        #staff_fname = row['first name'],
        #staff_lname = row['last name'],
        staff_email = row['all main researcher email']
    )
    department = Department(
        department_name=row['all department']
    )

    session.add(funding_sources)
    session.add(staff)
    session.add(department)
session.commit()

#--------------Research------------------------
research_df = read_excel('samplefunding.xlsx',sheet_name='funding')

for ix,row in research_df.iterrows():
    research = Research(
        research_title_th = row['research title thai'],
        research_title_en = row['research title eng'],
       # research_field = row['research_field'],
       # research_budget_thisyear = row['research_budget_thisyear'],
        est_funding = row['amount fund'],
        research_startdate = row['start date'],
        research_enddate = row['end date'],
      # duration = row['duration'],
        research_contract = row['research contract']
    )
    session.add(research)
session.commit()


#st = session.query(Staff).filter(Staff.staff_email=='napat.son').first()
#st = session.query(Staff).filter(Staff.staff_email==row['staff_email']).first()
#st.staff_id

#int(datetime.strftime(row['research_startdate'], '%Y%m%d'))


