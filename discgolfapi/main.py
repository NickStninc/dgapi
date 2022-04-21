from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal

from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/course')
def course_create(course : schemas.Course, db: Session = Depends(get_db)):
  new_course = models.Course(name=course.name, condition=course.condition, parkPhoto= course.parkPhoto, location=course.location,holes=course.holes,services=course.services, established=course.established, property=course.property, tees=course.tees, availability=course.availability, targets=course.targets)
  db.add(new_course)
  db.commit()
  db.refresh(new_course)
  return new_course



@app.post('/layout')
def layout_create(layout : schemas.Layout, db: Session = Depends(get_db)):
  new_layout = models.Layout(title=layout.title,totalHoles=layout.totalHoles, totalPar=layout.totalPar, totalFeet=layout.totalFeet,)
  db.add(new_layout)
  db.commit()
  db.refresh(new_layout)
  return new_layout


@app.post('/holes')
def holes_create(holes : schemas.Holes, db : Session = Depends(get_db)):
  new_holes = models.Holes(pictures=holes.pictures, number=holes.number, par=holes.par, feet=holes.feet, mandatory=holes.mandatory, hazzards = holes.hazzards, outOfBounds=holes.outOfBounds)
  db.add(new_holes)
  db.commit()
  db.refresh(new_holes)  
  return new_holes


@app.post('/routes')
def routes_create(routes : schemas.Routes):
  return routes


