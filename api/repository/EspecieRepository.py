from fastapi import Depends
from sqlalchemy.orm import Session
from models.Especie import Especie

class EspecieRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Especie).all()
    
    @staticmethod
    def salvar(db: Session, especie: Especie):
        if especie.especie_id:
            db.merge(especie)
        else:
            db.add(especie)
        db.commit()
        return especie
    
    @staticmethod
    def atualizar(db: Session, especie: Especie):
        if especie.especie_id:
            db.merge(especie)
            db.commit()
            return especie
    
    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Especie).filter(Especie.especie_id == id).first()
    
    @staticmethod
    def deletar(db: Session, id: int):
        especie = db.query(Especie).filter(Especie.especie_id == id).first()
        if especie is not None:
            db.delete(especie)
            db.commit()
            return True
        return False

    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Especie).filter(Especie.especie_id == id).first() is not None
