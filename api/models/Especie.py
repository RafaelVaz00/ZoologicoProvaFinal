from fastapi import Depends, FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

from models import DataBase

Base = declarative_base()

# Definição do modelo de tabela para Espécie
class Especie(Base):
    __tablename__ = "especies"

    especie_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_especie = Column(String(50), nullable=False)
    descricao = Column(String(255), nullable=True)
    habitat = Column(String(100), nullable=True)
    curiosidade = Column(String(255), nullable=True)
    dieta = Column(String(100), nullable=True)
    expectativa_vida_anos = Column(Integer)

class EspecieBase(BaseModel):
    especie_id: int
    nome_especie: str
    descricao: str
    habitat: str
    curiosidade: str
    dieta: str
    expectativa_vida_anos: int

class EspecieRequest(BaseModel):
    nome_especie: str
    descricao: str
    habitat: str
    curiosidade: str
    dieta: str
    expectativa_vida_anos: int


class EspecieResponse(BaseModel):
    especie_id: Optional[int]
    nome_especie: str
    descricao: str
    habitat: str
    curiosidade: str
    dieta: str
    expectativa_vida_anos: int

animais = relationship("animais", back_populates="especie")