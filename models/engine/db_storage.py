#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Defines the DBStorage class."""
    # __engine = None
    # __session = None

    # def __init__(self):
    #     """
    #     Initializes the DBStorage class.
    #     """
    #     user = getenv("HBNB_MYSQL_USER")
    #     passwd = getenv("HBNB_MYSQL_PWD")
    #     db = getenv("HBNB_MYSQL_DB")
    #     host = getenv("HBNB_MYSQL_HOST")
    #     env = getenv("HBNB_ENV")

    #     self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
    #                                   .format(user, passwd, host, db),
    #                                   pool_pre_ping=True)

    #     if getenv('HBNB_ENV') == 'test':
    #         Base.metadata.drop_all(self.__engine)

    # def all(self, cls=None):
    #     """
    #     Queries all objects of a certain class or all classes if no class is specified.
    #     """
    #     new_dict = {}
    #     if cls:
    #         objs = self.__session.query(cls).all()
    #     else:
    #         from models.state import State
    #         from models.city import City
    #         from models.user import User
    #         from models.place import Place
    #         from models.amenity import Amenity
    #         from models.review import Review
    #         classes = [State, City, User, Place, Amenity, Review]
    #         objs = []
    #         for cls in classes:
    #             objs.extend(self.__session.query(cls).all())
    #     for obj in objs:
    #         key = "{}.{}".format(type(obj).__name__, obj.id)
    #         new_dict[key] = obj
    #     return new_dict

    # def new(self, obj):
    #     """
    #     Adds an object to the current database session.
    #     """
    #     self.__session.add(obj)

    # def save(self):
    #     """
    #     Commits all changes of the current database session.
    #     """
    #     self.__session.commit()

    # def delete(self, obj=None):
    #     """
    #     Deletes an object from the current database session.
    #     """
    #     if obj:
    #         self.__session.delete(obj)

    # def reload(self):
    #     """
    #     Creates all tables in the database and creates the current database session from the engine.
    #     """
    #     Base.metadata.create_all(self.__engine)
    #     session_factory = sessionmaker(bind=self.__engine,
    #                                    expire_on_commit=False)
    #     Session = scoped_session(session_factory)
    #     self.__session = Session()

    # def close(self):
    #     """
    #     Calls remove()
    #     """
    #     self.__session.close()

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
