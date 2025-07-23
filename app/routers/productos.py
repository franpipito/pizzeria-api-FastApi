from fastapi import APIRouter
from models import producto 


router = APIRouter(prefix = "/api/productos", tags =["productos"])

listaProductos = []
contador_Id = 1


@router.get("/")
def listar_productos(): 
    return listaProductos
    
    

def crear_productos(ProductoCreate):
    
