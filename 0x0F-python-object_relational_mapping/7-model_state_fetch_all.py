#!/usr/bin/python3

"""import modules"""

import sys
from sqlalchemy import create_engine
from model.state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)
    session = session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
