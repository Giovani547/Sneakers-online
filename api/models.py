from pydantic import BaseModel

class Sneaker(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: bool = True
    talla: str = ""

class ConsultaWhatsApp(BaseModel):
    sneaker_id: int
    mensaje: str = "Hola, me interesa este par"