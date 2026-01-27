from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

##TODO: Step 3
# 1. Create a model with the tablename 'appointments'.
# 2. Include columns for ID, type, request_origin, date, and status
class Patient(db.Model):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    birthday: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(500))
    phone_number: Mapped[str] = mapped_column(String(15))

class Appointment(db.Model): #NEW TABLE
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    request_origin: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))