#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def cities_state():
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name to search
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    var = session.query(State, City).join(City).all()
    for i in var:
        print("{}: ({}) {}".format(i[0].__dict__['name'],
                                   i[1].__dict__['id'],
                                   i[1].__dict__['name']))
    session.close()

if __name__ == "__main__":
    cities_state()
    
