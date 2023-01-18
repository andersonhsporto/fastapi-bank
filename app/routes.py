from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud
from app.config import SessionLocal
from app.schemas import Response, RequestAccount

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/accounts")
async def get_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _account = crud.get_account(db, skip, limit)
    return Response(status="OK", code=200, message="Success", data=_account)


@router.post("/accounts")
async def create_account(request: RequestAccount, db: Session = Depends(get_db)):
    _account = crud.create_account(db, account=request.parameter)
    return Response(status="OK", code=200, message="Success", data=_account)
