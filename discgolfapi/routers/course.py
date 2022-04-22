from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database
from . import oauth2
from ..repository import course


from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/course",
    tags=["Course"],
)

#### THIS IS A GET ROUTE #####
@router.get("/", response_model=List[schemas.Course])
def all_courses(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return course.get_all(db)


#### THIS IS A GET{ID} ROUTE ####
@router.get("/{id}", status_code=200, response_model=schemas.Course)
def show(id: int, db: Session = Depends(database.get_db)):
    return course.show(id, db)


#### THIS IS A POST ROUTE ####
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Course, db: Session = Depends(database.get_db)):
    return course.create(request, db)


#### THIS IS A DELETE ROUTE ####
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return course.destroy(id, db)


#### THIS IS AN UPDATE ROUTE #####
@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Course, db: Session = Depends(database.get_db)):
    return course.update(id, request, db)
