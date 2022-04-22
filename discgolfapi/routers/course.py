from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, models, database

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/course",
    tags=["course"],
)


@router.post("/course", status_code=status.HTTP_201_CREATED, tags={"Course"})
def course_create(course: schemas.Course, db: Session = Depends(database.get_db)):
    new_course = models.Course(
        name=course.name,
        condition=course.condition,
        parkPhoto=course.parkPhoto,
        location=course.location,
        holes=course.holes,
        services=course.services,
        established=course.established,
        property=course.property,
        tees=course.tees,
        availability=course.availability,
        targets=course.targets,
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@router.put("/course/{id}", status_code=status.HTTP_202_ACCEPTED, tags={"Course"})
async def update(id, course: schemas.Course, db: Session = Depends(database.get_db)):
    updated_course = db.query(models.Course).filter(models.Course.id == id)

    if not updated_course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    updated_course.update(course.dict())
    db.commit()
    return "updated"


@router.delete("/course/{id}", status_code=status.HTTP_204_NO_CONTENT, tags={"Course"})
def destroy(id, db: Session = Depends(database.get_db)):
    course = db.query(models.Course).filter(models.Course.id == id)

    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"course with id {id} not found")

    course.delete(synchronize_session=False)
    db.commit()
    return "done"


@router.get("/course", status_code=200, response_model=List[schemas.Course], tags={"Course"})
def all_courses(db: Session = Depends(database.get_db)):
    courses = db.query(models.Course).all()

    return courses


@router.get("/course/{id}", status_code=200, response_model=schemas.Course, tags={"Course"})
def show(id, db: Session = Depends(database.get_db)):
    course = db.query(models.Course).filter(models.Course.id == id).first()

    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with the ID {id} is not available")
    return course
