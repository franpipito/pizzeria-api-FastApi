from fastapi import FastAPI
from app.routers import productos

app = FastAPI()

app.include_router(productos.router)

@app.get("/ping")
def ping():
    return {"mensaje": "pong"}
