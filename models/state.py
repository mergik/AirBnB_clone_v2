#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    # __tablename__ = "states"
    # name = Column(String(128), nullable=False)
    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    #     cities = relationship("City", backref="state", cascade="all, delete")
    # else:
    #     @property
    #     def cities(self):
    #         """Get cities for a specific state"""
    #         from models import storage
    #         all_cities = storage.all(City)
    #         state_cities = []
    #         for city in all_cities.values():
    #             if city.state_id == self.id:
    #                 state_cities.append(city)
    #         return state_cities
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
