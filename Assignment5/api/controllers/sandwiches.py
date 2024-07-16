from sqlalchemy.orm import Session
from ..models import models

def create_sandwich(db: Session, sandwich_data):
    db_sandwich = models.Sandwich(**sandwich_data.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def get_all_sandwiches(db: Session):
    return db.query(models.Sandwich).all()

def get_sandwich_by_id(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id: int, sandwich_data):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if db_sandwich.first() is None:
        return None
    db_sandwich.update(sandwich_data.dict(), synchronize_session=False)
    db.commit()
    return db_sandwich.first()

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if db_sandwich.first() is None:
        return None
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return {'message': 'Deleted successfully'}
