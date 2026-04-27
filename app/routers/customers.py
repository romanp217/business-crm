from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.customer import Customer
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()
@router.post("/customers")
def create_customer(name: str, email: str, phone: str, db: Session = Depends(get_db)):
    new_customer = Customer(name=name, email=email, phone=phone)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
