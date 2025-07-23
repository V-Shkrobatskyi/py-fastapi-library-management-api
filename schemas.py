from _pydatetime import date

from pydantic import BaseModel


class BooksBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BooksCreate(BooksBase):
    pass


class Books(BooksBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    books_id: int


class Author(AuthorBase):
    id: int
    books: Books

    class Config:
        orm_mode = True
