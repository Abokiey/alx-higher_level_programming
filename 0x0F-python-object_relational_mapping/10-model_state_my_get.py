#!/usr/bin/python3
"""prints the State object with passed as argument"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)

    """sessionmaker"""
    Base.metadata.create_all(engine)
    Session_maker = sessionmaker(bind=engine)
    session = Session_maker()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
