# FastAPI Basics

## Create & activate venv (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

## Install
pip install -r topics/fastapi_basics/requirements.txt

## Run
uvicorn topics.fastapi_basics.main:app --reload

## Docs
- Swagger: http://127.0.0.1:8000/docs
- ReDoc:   http://127.0.0.1:8000/redoc
