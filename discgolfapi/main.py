from fastapi import FastAPI, Depends, status, HTTPException, Response
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

# this is CRUD for Course Information
@app.post('/course', status_code=status.HTTP_201_CREATED)
def course_create(course : schemas.Course, db: Session = Depends(get_db)):
  new_course = models.Course(name=course.name, condition=course.condition, parkPhoto= course.parkPhoto, location=course.location,holes=course.holes,services=course.services, established=course.established, property=course.property, tees=course.tees, availability=course.availability, targets=course.targets)
  db.add(new_course)
  db.commit()
  db.refresh(new_course)
  return new_course


@app.get('/course', status_code=200)
def all_courses(db: Session = Depends(get_db)):
  courses = db.query(models.Course).all()

  return courses

@app.get('/course/{id}')
def show(id, db: Session = Depends(get_db)):
  course = db.query(models.Course).filter(models.Course.id == id).first()

  if not course:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Course with the ID {id} is not available")    
  return course





@app.delete('/course/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
  course = db.query(models.Course).filter(models.Course.id == id).delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/course/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, course: schemas.Course, db: Session = Depends(get_db)):
  db.query(models.Course).filter(models.Course.id == id).update(course.dict())
  db.commit()
  return 'updated'



#This is CRUD for Layout information
@app.post('/layout', status_code=status.HTTP_201_CREATED)
def layout_create(layout : schemas.Layout, db: Session = Depends(get_db)):
  new_layout = models.Layout(title=layout.title,totalHoles=layout.totalHoles, totalPar=layout.totalPar, totalFeet=layout.totalFeet,)
  db.add(new_layout)
  db.commit()
  db.refresh(new_layout)
  return new_layout


@app.post('/holes',  status_code=status.HTTP_201_CREATED)
def holes_create(holes : schemas.Holes, db : Session = Depends(get_db)):
  new_holes = models.Holes(picture=holes.picture, number=holes.number, par=holes.par, feet=holes.feet, mandatory=holes.mandatory, hazzards = holes.hazzards, outOfBounds=holes.outOfBounds)
  db.add(new_holes)
  db.commit()
  db.refresh(new_holes)  
  return new_holes


@app.post('/routes')
def routes_create(routes : schemas.Routes, db : Session = Depends(get_db)):
  new_routes= models.Routes(title=routes.title, content=routes.content, video=routes.video)
  db.add(new_routes)
  db.commit()
  db.refresh(new_routes) 
  return new_routes


