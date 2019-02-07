from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from research_models import *
from pandas import read_excel

engine = create_engine('sqlite:///research.db')
Session = sessionmaker(bind=engine)
session = Session()


def load_funding_resource(input_file, sheet_name=None):
    """ Read funding resources from the input file and add to the db if not exist.

    :param input_file:
    :param sheet_name:
    :return None:
    """
    df = read_excel(input_file, sheet_name=sheet_name)

    for source_name in df[df.columns[1]]:
        src_ = session.query(FundingSource).filter(
            FundingSource.source == source_name).first()
        if src_ is None:
            funding_source = FundingSource(source=source_name)
            session.add(funding_source)
    session.commit()

    '''
    staff = Staff(
        #staff_fname = row['first name'],
        #staff_lname = row['last name'],
        staff_email = row['all main researcher email']
    )
    department = Department(
        department_name=row['all department']
    )
    '''
    #session.add(staff)
    #session.add(department)

def load_funding_agency(input_file, sheet_name=None):
    df = read_excel(input_file, sheet_name=sheet_name)

    for agency_name in df[df.columns[2]]:
        ag = session.query(FundingAgency).filter(
            FundingAgency.name == agency_name).first()
        if ag is None:
            agency = FundingAgency(name=agency_name)
            session.add(agency)
    session.commit()


def load_researcher(input_file, sheet_name=None):
    """

    :param input_file:
    :param sheet_name:
    :return:
    """
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


if __name__ == '__main__':
    # load_funding_resource('samplefunding.xlsx', 'funding')
    load_funding_agency('samplefunding.xlsx', 'funding')
