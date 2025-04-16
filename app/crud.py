from app.models import Producto
from typing import List

# Simulación de una base de datos (puedes reemplazar esto con una base de datos real)
productos_db = []

def crear_producto(producto: Producto) -> Producto:
    productos_db.append(producto)
    return producto

def obtener_productos() -> List[Producto]:
    return productos_db

def actualizar_producto(producto_id: int, producto: Producto) -> Producto:
    for i, p in enumerate(productos_db):
        if i == producto_id:
            productos_db[i] = producto
            return producto
    return None

def eliminar_producto(producto_id: int) -> dict:
    if 0 <= producto_id < len(productos_db):
        productos_db.pop(producto_id)
        return {"message": "Producto eliminado"}
    return {"error": "Producto no encontrado"}
