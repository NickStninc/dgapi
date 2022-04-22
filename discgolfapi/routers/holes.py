# @app.post("/holes", status_code=status.HTTP_201_CREATED, tags={"Holes"})
# def holes_create(holes: schemas.Holes, db: Session = Depends(get_db)):
#     new_holes = models.Holes(
#         picture=holes.picture,
#         number=holes.number,
#         par=holes.par,
#         feet=holes.feet,
#         mandatory=holes.mandatory,
#         hazzards=holes.hazzards,
#         outOfBounds=holes.outOfBounds,
#     )
#     db.add(new_holes)
#     db.commit()
#     db.refresh(new_holes)
#     return new_holes
