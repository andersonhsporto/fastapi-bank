from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.api import crud
from app.database.config import SessionLocal
from app.schema.schemas import Response, RequestAccount

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/accounts/all")
async def get_all_account(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _account = crud.get_account(db, skip, limit)
    return Response(status="OK", code=200, message="Success", result=_account)


@router.get("/accounts")
async def get_account_by_id(
        id: int,
        page: int,
        size: int,
        initialDate: str | None = None,
        finalDate: str | None = None,
        operatorName: str | None = None,
        db: Session = Depends(get_db)
):
    _account = crud.get_account(db, id, page, size, initialDate, finalDate, operatorName)
    return Response(status="OK", code=200, message="Success", result=_account)


@router.post("/accounts")
async def create_account(request: RequestAccount, db: Session = Depends(get_db)):
    _account = crud.create_account(db, account=request.parameter)
    return Response(status="OK", code=200, message="Success", data=_account)


@router.get("/transfers")
async def get_transfers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _transfer = crud.get_transfers(db, skip, limit)
    return Response(status="OK", code=200, message="Success", result=_transfer)