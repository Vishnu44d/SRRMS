#from .meta import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Table, ForeignKeyConstraint, Boolean
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserCredential(Base):
    __tablename__ = 'user_credential'
    id = Column(Integer, Sequence('user_credential_id'), primary_key=True, unique=True, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    pwd_hash = Column(String(512))
    created_on = Column(DateTime(timezone=True), nullable=False)
    last_updated_on = Column(DateTime(timezone=True), nullable=False)


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, Sequence("user_profile_id"), primary_key = True, unique=True, nullable=False)
    name = Column(String(100))
    contact = Column(ARRAY(String(50)))
    google_id = Column(Integer, unique=True)
    user_credential_id = Column(Integer, ForeignKey("user_credential.id"), unique=True)
    created_on = Column(DateTime(timezone=True), nullable=False)
    last_updated_on = Column(DateTime(timezone=True), nullable=False)
