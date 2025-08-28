from pydantic import BaseModel

class StockQuery(BaseModel):
    ticker: str
    start_date: str
    end_date: str

class StockResponse(BaseModel):
    ticker: str
    price: float
    date: str  # keep as string for now (ISO yyyy-mm-dd)