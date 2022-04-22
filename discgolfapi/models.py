from sqlalchemy import Column, Integer, String, ForeignKey
from typing import Optional
from .database import Base
from sqlalchemy.orm import relationship



class Course(Base):
  __tablename__ = 'course'
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  condition = Column(String)
  parkPhoto = Column(String)
  location = Column(String)
  holes = Column(String)
  services = Column(String)
  established = Column(String)
  property = Column(String)
  tees = Column(String)
  availability = Column(String)
  targets = Column(String)
  layout = relationship("Layout")
  
  
  
  
class Layout(Base):
  __tablename__ = 'layout'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  total_holes = Column(String)
  total_par = Column(String)
  total_feet = Column(String)
  layout_Information = Column(String)
  course_id= Column(Integer, ForeignKey('course.id'))
  layout = relationship("Holes")
  
  

  
class Holes(Base):
  __tablename__ = 'holes'
  
  id = Column(Integer, primary_key=True, index=True)
  picture = Column(String)
  number = Column(String)
  par = Column(String)
  feet = Column(String)
  mandatory = Column(String)
  hazzards = Column[String]
  out_of_bounds = Column[String]
  layout_id= Column(Integer, ForeignKey('layout.id'))
  layout = relationship("Routes")
  
  



class Routes(Base):
  __tablename__ = 'routes'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  video = Column(String)
  holes_id= Column(Integer, ForeignKey('holes.id'))
  
