from pydantic import BaseModel

class Sneaker(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: bool = True

class Checkout(BaseModel):
    curp: str
    rfc: str
    sneaker_id: int