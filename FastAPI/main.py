from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List, Optional

class OrderBase(BaseModel):
    size: int = Field(..., ge=0, le=1000, description="Size of order")
    amount: int = Field(..., ge = 0, description='Cost for the order')
    customer: str = Field(..., description='Name of customer')
    order_date: Optional[date] = Field(default_factory = lambda : datetime.now().date())
    order_timestamp: Optional[datetime] = Field(default_factory =datetime.now, description='Time of order')
    is_active: Optional[str] = Field(None, description= 'Activity Status')

class Order(OrderBase):
    id:  int = Field(..., description="Order ID")


class OrderCreate(OrderBase):
    pass

orders = [
Order(id = 1, size = 10, amount = 157, customer= 'XYZ'),
Order(id = 2, size = 7, amount = 2400, customer= 'ABC'),
Order(id = 3, size = 90, amount = 190, customer= 'EFG')
]
    

a = []
print(max(a) + 1)
