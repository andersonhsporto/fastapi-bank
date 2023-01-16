from sqlalchemy import Column, Integer, String, DateTime, Float

from app.config import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))


class Transfer(Base):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True, index=True)
    transfer_date = Column(DateTime)
    value = Column(Float)
    type = Column(String(50))
    operator_name = Column(String(50))
