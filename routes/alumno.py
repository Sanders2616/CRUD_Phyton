from fastapi import APIRouter
from config.db import engine, conn
from models.alumno import alumnos
from schemas.alumno import Alumno

router = APIRouter()

@router.get('/getAll')
def obtenerAlumnos():
    result = conn.execute(alumnos.select()).fetchall()
    response = []
    for tuple in result:
        alumno = {
            "matricula":tuple[0],
            "nombre":tuple[1],
            "apellidos":tuple[2],
            "cuatrimestre":tuple[3],
            "promedio":tuple[4],
        }
        response.append(alumno)
    return response

@router.post('/insert')
def insertAlumno(alumno:Alumno):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res={
        "status":"Alumno insertado con éxito"
    }
    return res 

@router.get('/getOne/{matricula}')
def obtenerAlumno(matricula:int):
    student_tuple=conn.execute(alumnos.select().where(alumnos.c.matricula==matricula)).first()
    if student_tuple!=None:
        student_dict={
                "matricula":student_tuple[0],
                "nombre":student_tuple[1],
                "apellidos":student_tuple[2],
                "cuatrimestre":student_tuple[3],
                "promedio":student_tuple[4],
        }
        return student_dict
    else:
        res={
            "status":"Alumno no encontrado"
        }
        return res
    

@router.put('/updateOne/{matricula}')
def actualizarAlumno(alumno:Alumno,matricula):
    res=obtenerAlumno(matricula)
    print(res)
    if res.get("status")=="No existe el alumno":
        return res
    else:
        result=conn.execute(alumnos.update().values(dict(alumno)).where(alumnos.c.matricula==matricula)).last_updated_params()
        conn.commit()
    return result



@router.delete('/deleteone/{matricula}')
def eliminarAlumno(matricula):
     res=obtenerAlumno(matricula)
    print(res)
    if res.get("status")=="No existe el alumno":
        return res
    else:
        result=conn.execute(alumnos.delete().where(alumnos.c.matricula==matricula))
        conn.commit()
        res={
            "status":"Alumno eliminado"
        }
    return res