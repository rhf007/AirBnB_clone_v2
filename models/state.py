#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base 
from models.city import City
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from os import getenv



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

if getenv("HBNB_TYPE_STORAGE") != "db":
    @property
    def cities(self):
        """return the list of City objects from storage linked to the current State"""
        city = []
        for c in list(models.storage.all(City).values()):
            if c.state_id == self.id:
                city.append(c)
        return city