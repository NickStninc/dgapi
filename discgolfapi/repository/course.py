from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from .. import models, schemas


def get_all(db: Session):
    courses = db.query(models.Course).all()
    return courses


def create(request: schemas.Course, db: Session):
    new_course = models.Course(
        name=request.name,
        condition=request.condition,
        parkPhoto=request.parkPhoto,
        location=request.location,
        holes=request.holes,
        services=request.services,
        established=request.established,
        property=request.property,
        tees=request.tees,
        availability=request.availability,
        targets=request.targets,
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def destroy(id: int, db: Session):
    course = db.query(models.Course).filter(models.Course.id == id)

    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"course with id {id} not found")

    course.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Course, db: Session):
    course = db.query(models.Course).filter(models.Course.id == id)

    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {id} not found")

    course.update(request)
    db.commit()
    return f"This Blog id {id} was updated"


def show(id: int, db: Session):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with the ID {id} is not available")
    return course
