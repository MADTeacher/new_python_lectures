from database.configuration import Session, create_tables
from models.employee import Employee
from models.order import Order
from models.order_item import OrderItem
from models.pizza import Pizza
from models.shift import Shift


def create_db(set_mock_data: bool = True) -> None:
    create_tables()
    if set_mock_data:
        insert_mock_data()


def insert_mock_data() -> None:
    session = Session()

    pizzas = [
        Pizza(name="Margherita", description="Tomato sauce, mozzarella, basil", price=10.99),
        Pizza(name="Pepperoni", description="Tomato sauce, mozzarella, pepperoni", price=12.99),
        Pizza(name="Hawaiian", description="Tomato sauce, mozzarella, ham, pineapple", price=11.99),
        Pizza(name="Meat Feast", description="Tomato sauce, mozzarella, sausage, bacon, pepperoni", price=15.99),
    ]

    orders = [
        Order(name="John Smith", phone="(555) 555-1212", address="123 Main St, Anytown, USA"),
        Order(name="Jane Doe", phone="(555) 555-1313", address="456 Elm St, Anytown, USA"),
    ]



    employees = [
        Employee(
            name="David Johnson",
            position="Manager",
            shift=[Shift(start_time="09:00", end_time="17:00")],
        ),
        Employee(
            name="Sarah Lee",
            position="Chef",
            shift=[Shift(start_time="10:00", end_time="18:00")],
        ),
        Employee(
            name="Mark Smith",
            position="Waiter",
            shift=[Shift(start_time="12:00", end_time="20:00")]
        ),
    ]

    session.add_all(pizzas)
    session.add_all(orders)
    session.add_all(employees)
    session.flush()

    order_items = [
        OrderItem(
            pizza_id=pizzas[0].id,
            order_id=orders[0].id,
            quantity=2,
        ),
        OrderItem(
            pizza_id=pizzas[0].id,
            order_id=orders[0].id,
            quantity=1,
        ),
        OrderItem(
            pizza_id=pizzas[1].id,
            order_id=orders[1].id,
            quantity=3,
        ),
    ]


    session.add_all(order_items)
    session.commit()
    session.close()
