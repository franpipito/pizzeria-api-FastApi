from fastapi import APIRouter
from app.models.producto import Producto


router = APIRouter(prefix = "/productos", tags =["productos"])

lista_productos = [
    {"id": 1, "nombre": "Muzzarella"},
    {"id": 2, "nombre": "Napolitana"},
    {"id": 3, "nombre": "Provolone"}
]


@router.get("/")
def listar_productos(): 
    return lista_productos