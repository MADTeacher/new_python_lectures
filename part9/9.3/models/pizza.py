from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.configuration import Base


class Pizza(Base):
    __tablename__ = 'pizza'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[float]

    def __repr__(self) -> str:
        return f'Pizza [id={self.id} name={self.name} description={self.description} price={self.price}]'
