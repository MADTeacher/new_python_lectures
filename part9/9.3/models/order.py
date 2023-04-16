from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.configuration import Base


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(250))
    is_completed: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f'Order [id={self.id} name={self.name} phone={self.phone} ' \
               f'address={self.address} is_completed={self.is_completed}]'