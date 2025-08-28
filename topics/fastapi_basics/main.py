from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

from .models import StockQuery, StockResponse

app = FastAPI()

# --- Pydantic model (what we accept/return as JSON) ---
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., ge=0)       # >= 0
    is_offer: Optional[bool] = False      # optional
    tags: List[str] = []                  # optional list

# --- In-memory "DB" ---
items = ["apple", "banana", "orange"]     # from Step 2
store: list[Item] = []                    # holds created Item objects

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/items")
def read_items():
    # show both initial items and created ones (names only)
    return {"items": items + [i.name for i in store]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": f"This is item {item_id}"}

@app.get("/search")
def search_item(q: Optional[str] = None):
    if not q:
        return {"results": []}
    # choose your preferred policy; here is exact match:
    matches = [item for item in items if q.lower() == item.lower()]
    matches += [i.name for i in store if q.lower() == i.name.lower()]
    if matches:
        return {"results": matches}
    return {"results": [f"no {q} here"]}

# --- NEW: POST with JSON body ---
@app.post("/items", status_code=201)
def create_item(item: Item):
    # simple uniqueness check by name
    if any(i.name.lower() == item.name.lower() for i in store) or any(
        q.lower() == item.name.lower() for q in items
    ):
        raise HTTPException(status_code=409, detail="Item with this name already exists.")
    store.append(item)
    return {"message": "created", "item": item}
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo/{name}")
def echo(name: str):
    return {"hello": name}

@app.post("/query-stock")
def query_stock(query: StockQuery):
    # Pydantic v2 uses .model_dump(); if you’re on v1, replace with .dict()
    try:
        payload = query.model_dump()  # v2
    except AttributeError:
        payload = query.dict()        # v1 fallback
    return {"received": payload}

# --- NEW: typed response ---
@app.get("/get-stock/{ticker}", response_model=StockResponse)
def get_stock(ticker: str):
    # stubbed example; pretend we looked up today's price
    return StockResponse(
        ticker=ticker.upper(),
        price=123.45,
        date=str(date.today())
    )