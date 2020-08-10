#!/usr/bin/python3
"""List all State objects from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_all():
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    var = session.query(State).all()
    for i in var:
        print("{}: {}".format(i.__dict__['id'], i.__dict__['name']))
    session.close()

if __name__ == "__main__":
    list_all()
    