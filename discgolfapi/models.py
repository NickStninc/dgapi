from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    condition = Column(String(100))
    parkPhoto = Column(String(100))
    location = Column(String(100))
    holes = Column(String(100))
    services = Column(String(100))
    established = Column(String(100))
    property = Column(String(100))
    tees = Column(String(100))
    availability = Column(String(100))
    targets = Column(String(100))
    layouts = relationship("Layout", back_populates="course")


class Layout(Base):
    __tablename__ = "layout"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    totalHoles = Column(String(100))
    totalPar = Column(String(100))
    totalFeet = Column(String(100))
    layoutInformation = Column(String(100))
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", back_populates="layouts")


# class Holes(Base):
#     __tablename__ = "holes"

#     id = Column(Integer, primary_key=True, index=True)
#     picture = Column(String)
#     number = Column(String)
#     par = Column(String)
#     feet = Column(String)
#     mandatory = Column(String)
#     hazzards = Column[String]
#     out_of_bounds = Column[String]


# class Routes(Base):
#     __tablename__ = "routes"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     content = Column(String)
#     video = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
