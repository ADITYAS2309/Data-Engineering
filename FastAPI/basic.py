from fastapi import FastAPI, HTTPException
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

class OrderUpdate(BaseModel):
    size: Optional[int] = Field(None, ge=0, le=1000, description="Size of order")
    amount: Optional[int] = Field(None, ge = 0, description='Cost for the order')
    customer: Optional[str] = Field(None, description='Name of customer')
    order_date: Optional[date] = Field(default_factory = lambda : datetime.now().date())
    order_timestamp: Optional[datetime] = Field(default_factory =datetime.now, description='Time of order')
    is_active: Optional[str] = Field(None, description= 'Activity Status')



orders = [ 
    Order(id = 1, size = 10, amount = 157, customer= 'XYZ'),
    Order(id = 3, size = 90, amount = 190, customer= 'EFG'),
    Order(id = 2, size = 7, amount = 2400, customer= 'ABC')
]
    
#print(type(orders[0].order_date))   

api = FastAPI()


@api.get("/orders", response_model=List[Order])     
def get_orders(first_n: int = None):
    if first_n:
        return orders[:first_n]
    
    else:
        return orders[:3]
    

@api.get("/orders/{order_id}", response_model=Order)
def get_order(order_id : int):
    for order in orders:
        if order.id == order_id:
            return order
        
    raise HTTPException(status_code=404, detail='Not found')

    

@api.post("/orders", response_model = Order)
def create_order(new_order: OrderCreate):

    if orders:
        new_id = max(order.id for order in orders) + 1   
    else:   
        new_id = 1

    new_order = Order(id = new_id, **new_order.model_dump())
    orders.append(new_order)
    return new_order


@api.put("/orders", response_model=Order)
def update_order(id: int, updated_order: OrderUpdate):
    for order in orders:
        if order.id == id:
            if updated_order.size is not None:
                order.size = updated_order.size
            
            if updated_order.amount is not None:
                order.amount = updated_order.amount
            
            if updated_order.customer is not None:
                order.customer = updated_order.customer

            if updated_order.order_date is not None:
                order.order_date = updated_order.order_date  

            if updated_order.order_timestamp is not None:
                order.order_timestamp = updated_order.order_timestamp    

            if updated_order.is_active is not None:
                order.is_active = updated_order.is_active 

            return order    

    raise HTTPException(status_code=404, detail='Not found')
   

@api.delete("/orders", response_model=Order)
def delete_order(id: int):
    for index, order in enumerate(orders):
        if order.id == id:
            deleted_id = orders.pop(index)
            return deleted_id   

    raise HTTPException(status_code=404, detail='Not found')
