from sqlalchemy import select

from database.configuration import Session
from models.order import Order
from models.order_item import OrderItem
from models.pizza import Pizza


def add_order(name: str, phone: str, address: str) -> int:
    with Session() as session:
        order = Order(name=name, phone=phone, address=address)
        session.add(order)
        session.commit()
        return order.id


def add_order_item(pizza_id: int, order_id: int, quantity: int) -> None:
    with Session() as session:
        session.add(OrderItem(pizza_id=pizza_id, order_id=order_id, quantity=quantity))
        session.commit()


def set_completed_order(order_id: int) -> None:
    with Session() as session:
        order = session.get(Order, order_id)
        order.is_completed = True
        session.commit()


def get_completed_orders() -> list:
    return __get_orders_with_status(1)


def get_current_orders() -> list:
    return __get_orders_with_status(0)


def __get_orders_with_status(status: int) -> list:
    with Session() as session:
        orders = session.execute(
            select(
                Order.id,
                Order.name,
                Order.phone,
                Order.address,
                Order.is_completed,
            ).where(Order.is_completed == status)
        ).all()
        return orders


def get_orders() -> list:
    with Session() as session:
        orders = session.execute(
            select(
                Order.id,
                Order.name,
                Order.phone,
                Order.address,
                Order.is_completed,
            )
        ).all()
        return orders


def get_orders_with_pizzas(order_id: int) -> list:
    with Session() as session:
        orders = session.execute(
            select(
                Order.id,
                Order.is_completed,
                Order.name,
                Order.phone,
                Order.address,
                Pizza.name,
                OrderItem.quantity,
            ).join(
                OrderItem,
                OrderItem.order_id == Order.id,
            ).join(
                Pizza,
                Pizza.id == OrderItem.pizza_id,
            ).where(OrderItem.order_id == order_id)
        ).all()
        return orders
