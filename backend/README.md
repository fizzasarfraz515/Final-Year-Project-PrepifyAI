# PrepifyAI Backend

## Local setup

```bash
pip install -r requirements.txt
set PYTHONPATH=backend  # Windows CMD example
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker

```bash
cd backend
docker compose up --build
```

API will be available at `http://localhost:8000/api/health`.
