from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
items_db = {}

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q or "No query parameter"}

@app.get("/items/")
async def list_items(query: Optional[str] = None):
    return {"query": query}

@app.get("/items/{item_id}/query")
async def get_item_with_query(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q or "No query parameter"}

@app.post("/items/")
async def add_item(item: Item):
    item_id = str(len(items_db))
    items_db[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
async def modify_item(item_id: int, item: Item):
    if str(item_id) not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[str(item_id)] = item
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def remove_item(item_id: int):
    if str(item_id) not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[str(item_id)]
    return {"detail": "Item deleted"}
