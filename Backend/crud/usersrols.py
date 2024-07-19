import models.usersrols
import schemas.usersrols
from sqlalchemy.orm import Session
import models, schemas


def get_userrol_by_ids(db: Session, usuario_id: int, rol_id: int):
    return db.query(models.usersrols.UserRol).filter(
        models.usersrols.UserRol.Usuario_ID == usuario_id,
        models.usersrols.UserRol.Rol_ID == rol_id
    ).first()


def get_usersrols(db:Session, skip: int=0, limit:int=10):
    return db.query(models.usersrols.UserRol).offset(skip).limit(limit).all()


def create_userrol(db:Session, userrol: schemas.usersrols.UserRolCreate):
    db_userrol = models.usersrols.UserRol(Usuario_ID=userrol.Usuario_ID, 
                                          Rol_ID=userrol.Rol_ID,
                                          Estatus=userrol.Estatus, 
                                          Fecha_Registro=userrol.Fecha_Registro, 
                                          Fecha_Actualizacion=userrol.Fecha_Actualizacion)
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol


def update_userrol(db: Session, usuario_id: int, rol_id: int, userrol: schemas.usersrols.UserRolUpdate):
    db_userrol = db.query(models.usersrols.UserRol).filter(
        models.usersrols.UserRol.Usuario_ID == usuario_id,
        models.usersrols.UserRol.Rol_ID == rol_id
    ).first()
    if db_userrol:
        # Actualiza solo los campos deseados
        db_userrol.Estatus = userrol.Estatus
        db_userrol.Fecha_Registro = userrol.Fecha_Registro
        db_userrol.Fecha_Actualizacion = userrol.Fecha_Actualizacion

        db.commit()
        db.refresh(db_userrol)
    return db_userrol


def delete_userrol(db:Session,  usuario_id: int, rol_id: int):
    db_userrol = db.query(models.usersrols.UserRol).filter(models.usersrols.UserRol.Usuario_ID == usuario_id,
                                                           models.usersrols.UserRol.Rol_ID == rol_id
    ).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol