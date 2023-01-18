from sqlalchemy.orm import Session

from app.models import Account
from app.schemas import AccountSchema


def get_account(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Account).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Account).filter(Account.id == book_id).first()


def create_account(db: Session, account: AccountSchema):
    _account = Account(name=account.name)

    db.add(_account)
    db.commit()
    db.refresh(_account)
    return _account


def remove_account(db: Session, account_id: int):
    _account = get_book_by_id(db, account_id)

    db.delete(_account)
    db.commit()


def update_account(db: Session, account: Account):
    _account = get_book_by_id(db, account.id)

    _account.name = account.name
    db.commit()
    db.refresh(_account)
    return _account
