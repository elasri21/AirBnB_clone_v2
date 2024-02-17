#!/usr/bin/python3
""" Module to handle database"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """class to handle the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize an instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects in the current session
        Args:
            cls: class to work with its instances"""
        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        all_res = {}
        q_rows = []
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            q_rows = self.__session.query(cls)
            for ob in q_rows:
                k = '{}.{}'.format(type(ob).__name__, ob.id)
                all_res[k] = ob
            return all_res
        else:
            for key, value in classes.items():
                q_rows = self.__session.query(value)
                for ob in q_rows:
                    k = '{}.{}'.format(key, ob.id)
                    all_res[k] = ob
            return all_res

    def new(self, obj):
        """adds objects to the database
        Args:
            obj: objects to add to database"""
        self.__session.add(obj)

    def save(self):
        """commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from database
        Args:
            obj: object to be deleted"""
        self.__session.delete(obj)

    def reload(self):
        """Create database and its tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the current session"""
        self.__session.close()
