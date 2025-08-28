# FastAPI Basics (de-learning-lab)

## Endpoints
- `GET /` → `{"message":"Hello FastAPI"}`
- `GET /health` → `{"status":"ok"}`
- `GET /echo/{name}` → `{"hello": "<name>"}`
- `POST /query-stock` → body: `{ticker, start_date, end_date}` (Pydantic)
- `GET /get-stock/{ticker}` → returns `StockResponse {ticker, price, date}`

## Run
```bash
uvicorn fastapi_basics.main:app --reload
