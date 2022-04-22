from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/user", response_model=schemas.ShowUser, tags={"User"})
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=user.name, email=user.email, password=Hash.bycrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user


@router.get("/user/{id}", response_model=schemas.ShowUser, tags={"User"})
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the ID {id} is not available")
    return user
