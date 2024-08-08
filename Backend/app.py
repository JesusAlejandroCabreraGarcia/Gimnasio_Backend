from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import userrol
from routes.schedule import schedule
from routes.area import area
from routes.puestos import puesto
from routes.empleados import empleado

app = FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(schedule)
app.include_router(area)
app.include_router(puesto)
app.include_router(empleado)
print("Hola bienvenido a mi backend")