# Library Management System (FastAPI)

## Features
- Add a new book
- View all books
- View book by ID
- Update book
- Delete book

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy

## Run Locally

1. Install dependencies
pip install -r requirements.txt

2. Setup PostgreSQL DB

3. Run server
uvicorn app.main:app --reload

4. Open Swagger Docs
http://127.0.0.1:8000/docs
