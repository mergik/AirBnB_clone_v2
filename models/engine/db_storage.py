#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    """Defines the DBStorage class."""
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage class.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects of a certain class or all classes if no class is specified.
        """
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            from models.state import State
            from models.city import City
            from models.user import User
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review
            classes = [State, City, User, Place, Amenity, Review]
            objs = []
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        Adds an object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates the current database session from the engine.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
