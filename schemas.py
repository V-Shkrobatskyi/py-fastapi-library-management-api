from _pydatetime import date

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
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
