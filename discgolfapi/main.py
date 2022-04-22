from fastapi import FastAPI
from .database import engine
from . import models
from .routers import course, layout, holes, routes, user, auth

app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(course.router)
app.include_router(layout.router)
# app.include_router(holes.router)
# app.include_router(routes.router)
