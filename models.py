from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__: "user_tbl"

    name: Mapped[str] = mapped_column(String(30))

