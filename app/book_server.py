from fastapi import FastAPI
from typing import List, Optional
from book_data import books
import requests


app = FastAPI()

@app.get("/")
async def do_nothing():
    return {"message": "This route does nothing"}

@app.get("/api/", response_model=List[dict])
async def get_books(genre_contains: Optional[str] = None, author_contains: Optional[str] = None, title_contains: Optional[str] = None):
    selected_books = []
    for book in books:
        if ((genre_contains is None or genre_contains in book['genre'].lower()) and
            (author_contains is None or author_contains in book['author'].lower()) and
            (title_contains is None or title_contains in book['title'].lower())
        ):
            selected_books.append(book)
    return selected_books


