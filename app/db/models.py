from typing import Optional

from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)

class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)

    photos: Mapped["Photo"] = relationship("Photo", back_populates="task")

class Photo(Base):
    __tablename__ = 'photos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    filename: Mapped[str] = mapped_column(String, index=True)  # Название файла в MinIO
    url: Mapped[str] = mapped_column(String)  # Ссылка на фото в MinIO
    task_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tasks.id"))  # Связь с таблицей заданий

    task: Mapped[Task] = relationship("Task", back_populates="photos")
class Employee(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    patronymic: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    department: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    photo: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    schedules: Mapped["Schedule"] = relationship("Schedule", back_populates="employee")
    photos: Mapped["Photo"] = relationship("Photo", back_populates="employee")


class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id"))
    date: Mapped[str] = mapped_column(String)
    time_start: Mapped[str] = mapped_column(String)
    time_end: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    employee: Mapped[Employee] = relationship("Employee", back_populates="schedules")

