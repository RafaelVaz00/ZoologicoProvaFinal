from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session


DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:8080/zoologico"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Definição do modelo de tabela para Espécie
class Especie(Base):
    __tablename__ = "especies"

    especie_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_especie = Column(String)
    descricao = Column(String)
    habitat = Column(String)
    curiosidade = Column(String)
    dieta = Column(String)
    expectativa_vida_anos = Column(Integer)

    # Relacionamento bidirecional com a tabela Animal
    animais = relationship("Animal", back_populates="especie")

# Definição do modelo de tabela para Animal
class Animal(Base):
    __tablename__ = "animais"

    animal_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String)
    especie_id = Column(Integer, ForeignKey("especies.especie_id"))
    sexo = Column(String)
    data_nascimento = Column(String)

    # Relacionamento bidirecional com a tabela Especie
    especie = relationship("Especie", back_populates="animais")

# Definição do modelo Pydantic para a saída da rota
class AnimalOut(BaseModel):
    animal_id: int
    nome: str
    especie_id: int
    sexo: str
    data_nascimento: str

app = FastAPI()

def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

################################ Rota para inserir um novo animal#################################
@app.post("/animais/", response_model=AnimalOut)
async def create_animal(animal_in: AnimalOut):

    db = SessionLocal()
    
    # Criar uma instância de Animal com base nos dados recebidos
    animal = Animal(
        nome=animal_in.nome,
        especie_id=animal_in.especie_id,
        sexo=animal_in.sexo,
        data_nascimento=str(animal_in.data_nascimento)
    )

    db.add(animal)
    db.commit()
    db.refresh(animal)
    return animal


################################ Rota para obter um animal pelo ID ###################################
@app.get("/animais/{animal_id}", response_model=AnimalOut)
async def read_animal(animal_id: int, db: Session = Depends(get_connection)):
    animal = db.query(Animal).filter(Animal.animal_id == animal_id).first()
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal


@app.get("/")
def read_root():
    return {"message": "API está rodando"}
