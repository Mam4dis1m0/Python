from datetime import date
from pydantic import BaseModel, field_validator
from typing import List
from numpy import mean

class Estudiante(BaseModel):

    nombre: str
    identificacion: str
    fecha_nacimiento: date
    sexo: str
    notas: List[float]

    def obtener_edad(self) -> int:
        nacimiento = self.fecha_nacimiento
        actual = date.today()
        edad = actual.year - nacimiento.year if not actual.month < nacimiento.month or (nacimiento.month == actual.month and actual.day < nacimiento.day) \
            else actual.year - nacimiento.year - 1
        return edad

    def obtener_promedio(self) -> float:
        return mean(self.notas)

    @field_validator("nombre")
    def validar_nombre(cls, value):
        if value != "":

            return value
        raise ValueError("Debe ingresar un nombre!")


class EstudianteResponse(BaseModel):
    nombre: str = None
    identificacion: str = None
    edad: int = None
    sexo: str = None
    promedio: float = None
