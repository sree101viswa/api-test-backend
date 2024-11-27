from pydantic import BaseModel
from datetime import date

class CustomerBase(BaseModel):
    name: str
    age: int
    dob: date
    gender: str
    district: str
    mob: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        orm_mode = True



class DistrictResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

