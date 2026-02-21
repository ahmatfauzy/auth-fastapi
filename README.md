# FastAPI Authentication API

Secure, clean authentication API built with FastAPI and PostgreSQL.

## Installation

1. Clone repository ini

```bash
git clone https://github.com/ahmatfauzy/auth-fastapi.git
cd auth-fastapi
```

2. Buat virtual environment dan aktifkan

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirement.txt
```

4. Salin `.env.example` ke `.env` dan sesuaikan isinya

```bash
cp .env.example .env
```

5. Jalankan server

```bash
fastapi dev main.py
```

Server akan berjalan di `http://127.0.0.1:8000`

## API Documentation

Setelah server berjalan, buka:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| `GET` | `/` | Health check |
| `POST` | `/api/v1/auth/register` | Register user baru |
| `POST` | `/api/v1/auth/login` | Login dan dapatkan token |
| `GET` | `/api/v1/users/me` | Get current user (perlu token) |

## Struktur Folder

```
├── config/          # Konfigurasi dan environment settings
├── database/        # Database engine dan session
├── models/          # SQLAlchemy models
├── routes/          # API endpoints / routers
├── schemas/         # Pydantic schemas (request/response)
├── services/        # Business logic layer
├── utils/           # Utilities (security, hashing, JWT)
├── main.py          # Entry point aplikasi
├── requirement.txt  # Dependencies
├── .env             # Environment variables
└── .env.example     # Contoh environment variables
```