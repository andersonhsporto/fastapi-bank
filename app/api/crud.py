from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.accountDto import AccountDto
from app.models.models import Account, Transfer
from app.schema.schemas import AccountSchema


def get_all_account(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Account).offset(skip).limit(limit).all()


def get_account(db: Session,
                account_id: int,
                page: int,
                size: int,
                initial_date: str,
                final_date: str,
                operator_name: str):
    account_dto = AccountDto(
        id=account_id,
        name=None,
        page=page,
        size=size,
        initial_date=initial_date,
        final_date=final_date,
        operator_name=operator_name
    )
    if account_dto.is_valid_name_and_date():
        return _account_by_name_and_date(db, account_dto)
    elif account_dto.is_valid_date():
        return _account_by_date(db, account_dto)
    elif account_dto.is_valid_operator_name():
        return _account_by_operator_name(db, account_dto)
    else:
        return _account_by_id(db, account_dto)


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


def get_transfers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Transfer).offset(skip).limit(limit).all()


def _account_exists(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first() is not None


def _account_by_name_and_date(db: Session, account_dto: AccountDto):
    if _account_exists(db, account_dto.id) is False:
        raise HTTPException(status_code=404, detail="Account not found")

    return db.query(Transfer) \
        .filter(Transfer.account_id == account_dto.id) \
        .filter(Transfer.operator_name == account_dto.operator_name) \
        .filter(Transfer.date.between(account_dto.initial_date, account_dto.final_date)) \
        .offset(account_dto.page).limit(account_dto.size).all()


def _account_by_date(db: Session, account_dto: AccountDto):
    if _account_exists(db, account_dto.id) is False:
        raise HTTPException(status_code=404, detail="Account not found")

    return db.query(Transfer) \
        .filter(Transfer.account_id == account_dto.id) \
        .filter(Transfer.date.between(account_dto.initial_date, account_dto.final_date)) \
        .offset(account_dto.page).limit(account_dto.size).all()


def _account_by_operator_name(db: Session, account_dto: AccountDto):
    if _account_exists(db, account_dto.id) is False:
        raise HTTPException(status_code=404, detail="Account not found")

    return db.query(Transfer) \
        .filter(Transfer.account_id == account_dto.id) \
        .filter(Transfer.operator_name == account_dto.operator_name) \
        .offset(account_dto.page).limit(account_dto.size).all()


def _account_by_id(db: Session, account_dto: AccountDto):
    if _account_exists(db, account_dto.id) is False:
        raise HTTPException(status_code=404, detail="Account not found")

    return db.query(Transfer) \
        .filter(Transfer.account_id == account_dto.id) \
        .offset(account_dto.page).limit(account_dto.size).all()
