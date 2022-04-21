from pydantic import BaseModel
from typing import Optional


class Course(BaseModel):
  name : str
  condition : str
  parkPhoto : str
  location : str
  holes : str
  services : str
  established : str
  property : str
  tees : str
  availiability : str
  targets : str



class Layout(BaseModel):
  title : str
  totalHoles : str
  totalPar : str
  totalFeet : str
  
  
  
class Holes(BaseModel):
  picture : str
  number : str
  par : str
  feet : str
  mandatory : str
  hazzards : Optional[str] = None
  outOfBounds : Optional[str] = None
  
  
  
  
class Routes(BaseModel):
  title : str
  content : str
  video : str

