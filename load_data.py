import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from research_models import *
from pandas import read_excel

engine = create_engine('sqlite:///research.db')
Session = sessionmaker(bind=engine)
session = Session()

fund_df = read_excel('sample_fundingdata.xlsx', sheet_name='FundingSource')
for ix,row in fund_df.iterrows():
    fund = FundingSource(
        funding_source = row['funding_source'],
        funding_agency = row['funding_agency']
    )
    session.add(fund)
session.commit()

#--------------Staff---------------------------
#staff_df = read_excel('sample_fundingdata.xlsx', sheet_name='Staff')
#for ix,row in staff_df.iterrows():
#    st = Staff(
#        staff_firstname=row['staff_firstname'],
#        staff_lastname=row['staff_lastname'],
#        staff_email=row['staff_email'],
#        department_name=row['department_name']
#    )
#    session.add(st)
#session.commit()


#st = session.query(Staff).filter(Staff.staff_email=='napat.son').first()
#st = session.query(Staff).filter(Staff.staff_email==row['staff_email']).first()
#st.staff_id

#int(datetime.strftime(row['research_startdate'], '%Y%m%d'))



