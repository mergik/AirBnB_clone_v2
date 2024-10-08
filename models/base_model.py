#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    # def __init__(self, *args, **kwargs):
    #     """Instantiates a new model"""
    #     if not kwargs:
    #         self.id = str(uuid.uuid4())
    #         self.created_at = self.updated_at = datetime.utcnow()
    #     else:
    #         for key, value in kwargs.items():
    #             if key == "created_at" or key == "updated_at":
    #                 value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    #             setattr(self, key, value)

    # def __str__(self):
    #     """Returns a string representation of the instance"""
    #     cls = (str(type(self)).split('.')[-1]).split('\'')[0]
    #     return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    # def save(self):
    #     """Updates updated_at with current time when instance is changed"""
    #     from models import storage
    #     self.updated_at = datetime.utcnow()
    #     storage.new(self)
    #     storage.save()

    # def delete(self):
    #     """Delete the current instance from the storage"""
    #     from models import storage
    #     storage.delete(self)

    # def to_dict(self):
    #     """Convert instance into dict format"""
    #     dictionary = {}
    #     dictionary.update(self.__dict__)
    #     dictionary.update({'__class__': (
    #         str(type(self)).split('.')[-1]).split('\'')[0]})
    #     dictionary['created_at'] = self.created_at.isoformat()
    #     dictionary['updated_at'] = self.updated_at.isoformat()
    #     if '_sa_instance_state' in dictionary:
    #         del dictionary['_sa_instance_state']
    #     return dictionary


    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """ delete object
        """
        models.storage.delete(self)
