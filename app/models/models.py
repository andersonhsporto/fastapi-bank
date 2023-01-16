from sqlalchemy import Column, Integer, String, DateTime, Float

from app.config import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Transfer(Base):
    __tablename__ = 'transfers'

    id = Column(Integer, primary_key=True)
    transfer_date = Column(DateTime)
    value = Column(Float)
    type = Column(String(50))
    operator_name = Column(String(50))
