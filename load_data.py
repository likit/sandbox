import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from research_models import *
from pandas import read_excel

engine = create_engine('sqlite:///research.db')
Session = sessionmaker(bind=engine)
session = Session()


#fundingresearchfact_df = read_excel('sample_fundingdata.xlsx')

#for ix,row in fundingresearchfact_df.iterrows():
#    fundingresearchfact = FundingResearchFact(
#        research_name_th = row['research_name_th'],
#        research_name_en = row['research_name_en'],
#        research_field = row['research_field'],
#        research_budget_thisyear = row['research_budget_thisyear'],
#        research_budget_throughtout = row['research_budget_throughtout'],
#        research_startdate = int(datetime.strftime(row['research_startdate'], '%Y%m%d')),
#        research_enddate = int(datetime.strftime(row['research_enddate'], '%Y%m%d'))
#        # st = session.query(Staff).filter(Staff.staff_email=='napat.son').first()
#        # st = session.query(Staff).filter(Staff.staff_email==row['staff_email']).first()
#        # st.staff_id
#    )
#    session.add(fundingresearchfact)
#session.commit()


#--------------ResearchwithFund---------------------------
researchwithfund_df = read_excel('sample_fundingdata.xlsx',sheet_name='ResearchwithFund')
for ix,row in researchwithfund_df.iterrows():
    researchwithfund = ResearchwithFund(
        research_name_th = row['research_name_th'],
        research_name_en = row['research_name_en'],
        research_field = row['research_field'],
        research_budget_thisyear = row['research_budget_thisyear'],
        research_budget_throughtout = row['research_budget_throughtout'],
        research_startdate = int(datetime.strftime(row['research_startdate'], '%Y%m%d')),
        research_enddate = int(datetime.strftime(row['research_enddate'], '%Y%m%d')),
        duration = row['duration'],
        funding_contract = row['funding_contract']
    )
    session.add(researchwithfund)
session.commit()

#--------------FundingSource---------------------------
fund_df = read_excel('sample_fundingdata.xlsx', sheet_name='FundingSource')
for ix,row in fund_df.iterrows():
    fund = FundingSource(
        funding_source = row['funding_source'],
        funding_agency = row['funding_agency']
    )
    session.add(fund)
session.commit()

#--------------Staff---------------------------
staff_df = read_excel('sample_fundingdata.xlsx', sheet_name='Staff')
for ix,row in staff_df.iterrows():
    st = Staff(
        staff_firstname=row['staff_firstname'],
        staff_lastname=row['staff_lastname'],
        staff_email=row['staff_email'],
        department_name=row['department_name']
    )
    session.add(st)
session.commit()


#st = session.query(Staff).filter(Staff.staff_email=='napat.son').first()
#st = session.query(Staff).filter(Staff.staff_email==row['staff_email']).first()
#st.staff_id

#int(datetime.strftime(row['research_startdate'], '%Y%m%d'))


