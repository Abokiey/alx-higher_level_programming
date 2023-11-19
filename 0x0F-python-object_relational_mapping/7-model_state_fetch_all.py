#!/usr/bin/python3

"""import modules"""

import sys
from sqlalchemy import create_engine
from model.state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+pymysql://root:password@localhost:3306/hbtn_0e_6_usa")

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(state)

    session.close()
