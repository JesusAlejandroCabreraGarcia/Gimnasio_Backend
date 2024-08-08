from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
from portadortoken import Portador
import crud.persons, config.db, schemas.persons, models.persons
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

person = APIRouter()
models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@person.get('/persons/', response_model=List[schemas.persons.Person],tags=['Personas'],dependencies=[Depends(Portador())])
def read_persons(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_persons = crud.persons.get_persons(db=db,skip=skip, limit=limit)
    return db_persons

@person.post("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"],dependencies=[Depends(Portador())])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person= crud.persons.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@person.post('/persons/', response_model=schemas.persons.Person,tags=['Personas'])
def create_person(person: schemas.persons.PersonCreate, db: Session=Depends(get_db)):
    db_persons = crud.persons.get_person_by_nombre(db,nombre=person.Nombre)
    if db_persons:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)


@person.put('/persons/{id}', response_model=schemas.persons.Person,tags=['Personas'],dependencies=[Depends(Portador())])
def update_person(id:int,person: schemas.persons.PersonUpdate, db: Session=Depends(get_db)):
    db_persons = crud.persons.update_person(db=db, id=id, person=person)
    if db_persons is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo actualizar ")
    return db_persons


@person.delete('/persons/{id}', response_model=schemas.persons.Person,tags=['Personas'],dependencies=[Depends(Portador())])
def delete_person(id:int, db: Session=Depends(get_db)):
    db_persons = crud.persons.delete_person(db=db, id=id)
    if db_persons is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar ")
    return db_persons