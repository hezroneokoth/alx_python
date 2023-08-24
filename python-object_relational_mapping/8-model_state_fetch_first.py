#!/usr/bin/python3
"""
script prints the first State object from hbtn_0e_6_usa db
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

    # queries & prints the 1st state object
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # closes session
    session.close()
