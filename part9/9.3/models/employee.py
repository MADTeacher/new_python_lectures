from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.configuration import Base


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    position: Mapped[str] = mapped_column(String(100))
    shift: Mapped[list["Shift"]] = relationship(
        back_populates="employee",
        cascade="all, delete, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'Employee [id={self.id} name={self.name} position={self.position}]'
