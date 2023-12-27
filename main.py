import typing
from fastapi.middleware.cors import CORSMiddleware
import numpy
from fastapi import FastAPI
from mis_clases.estudiante import Estudiante, EstudianteResponse
from pydantic import BaseModel, ValidationError
from data.estudiantes import Estudiantes

import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/registrar")
def my_function(estudiante: Estudiante):
    response = EstudianteResponse()
    response.edad = estudiante.obtener_edad()
    response.identificacion = estudiante.identificacion
    try:
        response.nombre = estudiante.nombre
    except ValidationError as e:
        return ValueError("Debe ingresar un nombre!", e)

    response.sexo = estudiante.sexo
    response.promedio = estudiante.obtener_promedio()
    return dict(response)


@app.get("/filtrar")
def filtrar(calificacion: int) -> typing.List:
    return [estudiante.nombre for estudiante in Estudiantes if numpy.mean(estudiante.notas) >= calificacion]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

