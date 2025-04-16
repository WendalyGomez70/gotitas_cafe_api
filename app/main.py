from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.staticfiles import StaticFiles
from app.models import Producto
from app import crud



# Crear una instancia de FastAPI
app = FastAPI(
    title="Gestión de Productos",
    description="API para crear, leer, actualizar y eliminar productos.",
    version="1.0.0"
)

# Montar la carpeta "static" para servir los archivos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def leer_raiz():
    return {"mensaje": "Bienvenido a la API de productos!"}

@app.post("/productos/", response_model=Producto, summary="Crear un producto", tags=["Productos"])
async def crear_producto(producto: Producto):
    return crud.crear_producto(producto)

@app.get("/productos/", response_model=List[Producto], summary="Obtener todos los productos", tags=["Productos"])
def leer_productos():
    return crud.obtener_productos()

@app.put("/productos/{producto_id}", response_model=Producto, summary="Actualizar un producto", tags=["Productos"])
def actualizar_producto(producto_id: int, producto: Producto):
    resultado = crud.actualizar_producto(producto_id, producto)
    if resultado:
        return resultado
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{producto_id}", summary="Eliminar un producto", tags=["Productos"])
def eliminar_producto(producto_id: int):
    resultado = crud.eliminar_producto(producto_id)
    if resultado:
        return {"mensaje": "Producto eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
