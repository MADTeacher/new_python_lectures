from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.configuration import Base


class OrderItem(Base):
    __tablename__ = 'order_item'

    id: Mapped[int] = mapped_column(primary_key=True)
    pizza_id: Mapped[int] = mapped_column(ForeignKey('pizza.id'))
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    quantity: Mapped[int]

    def __repr__(self):
        return f'OrderItem [pizza_id={self.pizza_id} order_id={self.order_id} ' \
               f'quantity={self.quantity}]'
