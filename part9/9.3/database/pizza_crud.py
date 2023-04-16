from sqlalchemy import select

from database.configuration import Session
from models.pizza import Pizza


def add_pizza(name: str, description: str, price: float) -> None:
    with Session() as session:
        pizza = Pizza(name=name, description=description, price=price)
        session.add(pizza)
        session.commit()


def delete_pizza(pizza_id: int) -> None:
    with Session() as session:
        pizza = session.query(Pizza).filter_by(id=pizza_id).first()
        session.delete(pizza)
        session.commit()


def get_pizzas() -> list:
    with Session() as session:
        pizzas = session.execute(
            select(
                Pizza.id,
                Pizza.name,
                Pizza.description,
                Pizza.price
            )
        ).all()
        return pizzas


def get_pizzas_by_price(max_price: float) -> list:
    with Session() as session:
        return session.execute(
            select(
                Pizza.id,
                Pizza.name,
                Pizza.description,
                Pizza.price
            ).where(Pizza.price >= max_price)
        ).all()


def get_sort_pizzas_by_price() -> list:
    with Session() as session:
        return session.execute(
            select(
                Pizza.id,
                Pizza.name,
                Pizza.description,
                Pizza.price
            ).order_by(Pizza.price)
        ).all()


def change_pizza_name(pizza_id: int, new_name: str) -> None:
    with Session() as session:
        pizza = session.get(Pizza, pizza_id)
        pizza.name = new_name
        session.commit()


def change_pizza_description(pizza_id: int, new_description: str) -> None:
    with Session() as session:
        pizza = session.get(Pizza, pizza_id)
        pizza.description = new_description
        session.commit()


def change_pizza_price(pizza_id: int, new_price: float) -> None:
    with Session() as session:
        pizza = session.get(Pizza, pizza_id)
        pizza.price = new_price
        session.commit()
