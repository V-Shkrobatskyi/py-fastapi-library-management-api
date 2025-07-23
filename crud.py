from sqlalchemy.orm import Session

from db import models
import schemas
from db.models import PackagingType


def get_all_authors(db: Session):
    return db.query(models.Author).all()


def get_book_by_author_id(db: Session, author_id: str):
    return (
        db.query(models.Author).filter(models.Author.id == author_id).first()
    )


def create_author(db: Session, author: schemas.AuthorCreate):
    db_create_author = models.Author(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_create_author)
    db.commit()
    db.refresh(db_create_author)

    return db_create_author


def get_book_list(
    db: Session,
    author_id: int | None = None,
):
    queryset = db.query(models.Book)

    if author_id is not None:
        queryset = queryset.filter(models.Book.author_id=author_id)

    return queryset.all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
