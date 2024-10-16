from sqlalchemy import String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str | None] = mapped_column(nullable=True)
    phonenumber: Mapped[int | None] = mapped_column(nullable=True)
    link: Mapped[str | None] = mapped_column(String(255), nullable=True)