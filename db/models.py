from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from .database import Base


class UsersTable(Base):
    __tablename__ = "UsersTable"

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String)
    email = Column('email', String)
    created_at = Column('created_at', Numeric)
