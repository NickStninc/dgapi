from pydantic import BaseModel
from typing import Optional, List

# class Holes(BaseModel):
#     picture: str
#     number: str
#     par: str
#     feet: str
#     mandatory: str
#     hazzards: Optional[str] = None
#     outOfBounds: Optional[str] = None


# class Routes(BaseModel):
# title: str
# content: str
# video: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class Layout(BaseModel):
    title: str
    totalHoles: str
    totalPar: str
    totalFeet: str
    layoutInformation: str

    class Config:
        orm_mode = True


class Course(BaseModel):
    name: str
    condition: str
    parkPhoto: str
    location: str
    holes: str
    services: str
    established: str
    property: str
    tees: str
    availability: str
    targets: str
    layouts: List[Layout] = []

    class Config:
        orm_mode = True
