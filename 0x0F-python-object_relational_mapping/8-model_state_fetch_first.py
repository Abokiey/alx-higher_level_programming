#!/usr/bin/python3

'''print first obj from db'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session_maker = sessionmaker(bind=engine)
    session = Session_maker()

    first_obj = session.query(State).order_by(State.id).first()
    if first_obj:
        print("{:d}: {:s}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")

    session.close()
