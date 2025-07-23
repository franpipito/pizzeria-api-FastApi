from pydantic import BaseModel



class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    cantidad: int
    
    
class Producto(ProductoCreate):
    id: int
    
    
    class Config: 
        orm_mode = True

