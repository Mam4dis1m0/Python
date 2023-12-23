import typing

import numpy
from fastapi import FastAPI
from mis_clases.estudiante import Estudiante, EstudianteResponse
from pydantic import BaseModel, ValidationError
from data.estudiantes import Estudiantes

import uvicorn

app = FastAPI()

@app.post("/registrar")
def my_function(estudiante: Estudiante) -> dict:
    response = EstudianteResponse()
    response.nombre = estudiante.nombre
    response.identificacion = estudiante.identificacion
    try:
        response.edad = estudiante.obtener_edad()
    except ValidationError as e:
        print(e)

    response.sexo = estudiante.sexo
    response.promedio = estudiante.obtener_promedio()
    return dict(response)

@app.get("/")
def myget(identificacion: str):
    return next(filter(lambda estudiante: estudiante.identificacion == identificacion, Estudiantes), None)

@app.get("/filtrar")
def filtrar(calificacion: int) -> typing.List:
    return [estudiante.nombre for estudiante in Estudiantes if numpy.mean(estudiante.notas) >= calificacion]



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

