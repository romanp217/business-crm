from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.invoice import Invoice

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/invoices")
def get_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()

@router.post("/invoices")
def create_invoice(customer_id: int, amount: float, description: str, db: Session = Depends(get_db)):
    new_inv = Invoice(customer_id=customer_id, amount=amount, description=description)
    db.add(new_inv)
    db.commit()
    db.refresh(new_inv)
    return new_inv
