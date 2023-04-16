from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.configuration import Base


class Shift(Base):
    __tablename__ = 'shift'

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(
        ForeignKey('employee.id', ondelete='CASCADE')
    )
    start_time: Mapped[str] = mapped_column(String(5))
    end_time: Mapped[str] = mapped_column(String(5))

    employee: Mapped["Employee"] = relationship(
        back_populates="shift"
    )

    def __repr__(self) -> str:
        return f'Shift [id={self.id} employee_id={self.employee_id} ' \
               f'start_time={self.start_time} end_time={self.end_time}]'
