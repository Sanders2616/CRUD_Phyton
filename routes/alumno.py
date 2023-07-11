from fastapi import APIRouter
from config.db import engine, conn
from models.alumno import alumnos
from schemas.alumno import Alumno
router=APIRouter()

#Servicio para aobtener todos los alumnos
@router.get('/getAll')
def ObtenerAlumnos():
    result=conn.execute(alumnos.select()).fetchall()
    response=[]
    for tuple in result:
        alumno={
            "matricula":tuple[0],
            "nombre":tuple[1],
            "apellidos":tuple[2],
            "cuatrimestre":tuple[3],
            "promedio":tuple[4]
        }
        response.append(alumno)
        return response

@router.post('/insert')
def insertAlumno(alumno:Alumno):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res={
        "status":"Alumno Insertado Con Exito!"
    }
    return res