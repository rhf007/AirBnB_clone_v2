#!/usr/bin/python3
"""Define storage engine using MySQL database
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv

class DBStorage:
    """DB Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """init function"""
        uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
              getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
	      getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(uri, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """the all function"""
        classdictionary = {}
        from console import HBNBCommand

        if cls is None:
            for key in HBNBCommand.classes:
                if key != "BaseModel":
                    value = HBNBCommand.classes[key]
                for r in self.__session.query(value).all():
                  classdictionary.update({'{}.{}'.format(key, r.id): r})
            return classdictionary
        else:
            if cls is not BaseModel:
                for r in self.__session.query(cls).all():
                    classdictionary.update({'{}.{}'.format(cls, r.id): r})
            return classdictionary

    def new(self, obj):
        """add new"""
        self.__session.add(obj)

    def save(self):
        """saving/committing"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleting"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloading"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Sess = scoped_session(sess)
        self.__session = Sess()
    def close(self):
        """closing"""
        self.__session.close()
