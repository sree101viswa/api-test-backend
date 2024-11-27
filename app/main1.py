

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Customer
from schemas import CustomerResponse

# Initialize FastAPI app
app = FastAPI()

@app.get("/customerlist/", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    # Query the database to get all customers
    customers = db.query(Customer).all()
    
    # If no customers found, raise an exception
    if not customers:
        raise HTTPException(status_code=404, detail="No customers found")
    
    return customers