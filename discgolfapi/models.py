from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Course(Base):
    __tablename__ = "course"

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
    layouts = relationship("Layout", back_populates="course")


class Layout(Base):
    __tablename__ = "layout"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    totalHoles = Column(String)
    totalPar = Column(String)
    totalFeet = Column(String)
    layoutInformation = Column(String)
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
    name = Column(String)
    email = Column(String)
    password = Column(String)
