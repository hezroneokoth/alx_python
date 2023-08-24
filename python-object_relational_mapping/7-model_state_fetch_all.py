#!/usr/bin/python3
"""
script lists all state objects from hbtn_0e_6_usa db
"""

# import statements
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # creates the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name
                                   ), pool_pre_ping=True)

    # creates session
    Session = sessionmaker(bind=engine)
    session = Session()

    # queries & prints state objects
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # closes session
    session.close()
