from fastapi import FastAPI

from Arcitecture.Seminar_10.clinic.database.prepare_schema import PrepareDatabase
from Arcitecture.Seminar_10.clinic.routers import client_router, pet_router, consult_router
# from Arcitecture.Seminar_10.clinic.services.db import database

app = FastAPI()
create_db = PrepareDatabase()
create_db.prepare_db()

# @app.on_event('startup')
# async def startup():
#     await database.connect()
#
#
# @app.on_event('shutdown')
# async def shutdown():
#     await database.disconnect()
#

app.include_router(client_router.router, tags=['clients'])
# app.include_router(pet_router.router, tags=['pets'])
# app.include_router(consult_router.router, tags=['consultations'])

#
# @app.get('/')
# async def index():
#     return RedirectResponse(url='/docs')
