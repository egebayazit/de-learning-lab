from fastapi import FastAPI

app = FastAPI(title="FastAPI Basics Sandbox")

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
