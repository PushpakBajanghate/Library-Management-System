from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management System")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Book
@app.post("/books/", response_model=schemas.BookResponse)
def create(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

# Get All Books
@app.get("/books/", response_model=list[schemas.BookResponse])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

# Get Single Book
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update Book
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

# Delete Book
@app.delete("/books/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
