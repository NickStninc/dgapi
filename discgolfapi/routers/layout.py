from fastapi import APIRouter, Depends, status
from .. import schemas, models, database

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/layout",
    tags=["layout"],
)


@router.post("/layout", status_code=status.HTTP_201_CREATED, tags={"Layout"})
def layout_create(layout: schemas.Layout, db: Session = Depends(database.get_db)):
    new_layout = models.Layout(
        title=layout.title,
        totalHoles=layout.totalHoles,
        totalPar=layout.totalPar,
        totalFeet=layout.totalFeet,
        layoutInformation=layout.layoutInformation,
    )
    db.add(new_layout)
    db.commit()
    db.refresh(new_layout)
    return new_layout
