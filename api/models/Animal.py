
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

from models.Especie import Especie

Base = declarative_base()

class Animal(Base):
    __tablename__ = "animais"

    animal_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    especie_id = Column(Integer, ForeignKey(Especie.especie_id))
    sexo = Column(String(1), nullable=True)
    data_nascimento = Column(String(10), nullable=True)

    

# Definição do modelo Pydantic para a saída da rota
class AnimalBase(BaseModel):
    animal_id: int
    nome: str
    especie_id: int
    sexo: str
    data_nascimento: str

class AnimalRequest(BaseModel):
    nome: str
    especie_id: int
    sexo: str
    data_nascimento: str


class AnimalResponse(BaseModel):
    animal_id: Optional[int]
    nome: str
    especie_id: int
    sexo: str
    data_nascimento: str

    class Config:
        orm_mode = True

especie = relationship("especies", back_populates="animais")

