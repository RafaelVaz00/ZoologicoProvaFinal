from __future__ import annotations
from sqlalchemy.orm import Session
from models.Animal import Animal

class AnimalRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Animal).all()
    
    @staticmethod
    def salvar(db: Session, animal: Animal):
        if animal.animal_id:
            db.merge(animal)
        else:
            db.add(animal)
        db.commit()
        return animal
    
    @staticmethod
    def atualizar(db: Session, animal: Animal):
        if animal.animal_id:
            db.merge(animal)
            db.commit()
            return animal
    
    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Animal).filter(Animal.animal_id == id).first()
    
    @staticmethod
    def deletar(db: Session, id: int):
        animal = db.query(Animal).filter(Animal.animal_id == id).first()
        if animal is not None:
            db.delete(animal)
            db.commit()
            return True
        return False

    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Animal).filter(Animal.animal_id == id).first() is not None