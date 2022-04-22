# @app.post("/routes", tags={"Routes"})
# def routes_create(routes: schemas.Routes, db: Session = Depends(get_db)):
#     new_routes = models.Routes(title=routes.title, content=routes.content, video=routes.video)
#     db.add(new_routes)
#     db.commit()
#     db.refresh(new_routes)
#     return new_routes
