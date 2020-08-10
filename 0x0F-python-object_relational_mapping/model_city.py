#!/usr/bin/python3
"""Class definition of a state and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """Class for City"""
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
