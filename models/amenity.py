#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class
    Args:
        BaseModel: class to inherits from
        Base: class to inherits from"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
