from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from models.DataBase import get_connection
from models.Animal import AnimalBase
from models import Animal
from models.Animal import Animal, AnimalBase, AnimalRequest, AnimalResponse
from models.Especie import Especie, EspecieRequest, EspecieResponse
from models.DataBase import Base, engine, get_connection
from repository.AnimalRepository import AnimalRepository
from repository.EspecieRepository import EspecieRepository



Base.metadata.create_all(bind=engine)
app = FastAPI()


#Endpoints Animal
@app.get("/animais/todos", response_model=list[AnimalBase])
async def retorna_todos_animais(db: Session = Depends(get_connection)):
    return AnimalRepository.get_all(db)

@app.post("/animais/", response_model=AnimalResponse)
async def create_animal(request: AnimalRequest, db: Session = Depends(get_connection)):
    animal = Animal(
        nome=request.nome,
        especie_id=request.especie_id,
        sexo=request.sexo,
        data_nascimento=request.data_nascimento
    )
    return AnimalRepository.salvar(db, animal)

@app.get("/animais/{animal_id}", response_model=AnimalResponse)
async def obter_animal_por_id(animal_id: int, db: Session = Depends(get_connection)):
    
    animal = AnimalRepository.get_by_id(db, animal_id)
    
    if animal is None:
        raise HTTPException(status_code=404, detail="O Animal não foi encontrado ou não existe!")
    return animal

@app.delete("/animais/{animal_id}",status_code=status.HTTP_204_NO_CONTENT)
def deletar_animal(animal_id: int, db:Session = Depends(get_connection)):
    if not AnimalRepository.exists_by_id(db, animal_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Animal não encontrado.')
    if AnimalRepository.deletar(db, animal_id):
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Animal deletado com sucesso!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Não foi possível deletar o Animal.')

@app.put("/animais/{animal_id}", response_model=AnimalResponse)
async def create_animal(animal_id: int, request: AnimalRequest, db: Session = Depends(get_connection)):
    if not AnimalRepository.exists_by_id(db, animal_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contato não encontrado')
    
    animal = Animal(
        nome=request.nome,
        especie_id=request.especie_id,
        sexo=request.sexo,
        data_nascimento=request.data_nascimento
    )
    return AnimalRepository.atualizar(db, animal)


#Endpoints Especie

@app.get("/especies/todas", response_model=list[EspecieResponse])
async def retorna_todas_especies(db: Session = Depends(get_connection)):
    return EspecieRepository.get_all(db)

@app.post("/especies/", response_model=EspecieResponse)
async def criar_especie(request: EspecieRequest, db: Session = Depends(get_connection)):
    especie = Especie(
        nome_especie=request.nome_especie,
        descricao=request.descricao,
        habitat=request.habitat,
        curiosidade=request.curiosidade,
        dieta=request.dieta,
        expectativa_vida_anos=request.expectativa_vida_anos
    )
    return EspecieRepository.salvar(db, especie)

@app.get("/especies/{especie_id}", response_model=EspecieResponse)
async def obter_especie_por_id(especie_id: int, db: Session = Depends(get_connection)):
    especie = EspecieRepository.get_by_id(db, especie_id)
    if especie is None:
        raise HTTPException(status_code=404, detail="A espécie não foi encontrada ou não existe!")
    return especie

@app.delete("/especies/{especie_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_especie(especie_id: int, db: Session = Depends(get_connection)):
    if not EspecieRepository.exists_by_id(db, especie_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Espécie não encontrada.')
    if EspecieRepository.deletar(db, especie_id):
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Espécie deletada com sucesso!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Não foi possível deletar a espécie.')

@app.put("/especies/{especie_id}", response_model=EspecieResponse)
async def atualizar_especie(especie_id: int, request: EspecieRequest, db: Session = Depends(get_connection)):
    if not EspecieRepository.exists_by_id(db, especie_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Espécie não encontrada')
    
    especie = Especie(
        especie_id=especie_id,
        nome_especie=request.nome_especie,
        descricao=request.descricao,
        habitat=request.habitat,
        curiosidade=request.curiosidade,
        dieta=request.dieta,
        expectativa_vida_anos=request.expectativa_vida_anos
    )
    return EspecieRepository.atualizar(db, especie)
