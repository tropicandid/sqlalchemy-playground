from extensions import db
from sqlalchemy import Integer, String, Column, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column

##TODO: Step 4
# 1. Create a one to many relationship between the 'patients' and 'appointments' tables.
class Patient(db.Model):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    birthday: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(500))
    phone_number: Mapped[str] = mapped_column(String(15))
    appointments: Mapped[List["Appointment"]] = relationship(secondary='patient_appointments', back_populates="patient") #NEW LINE

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    request_origin: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    patient: Mapped[List["Patient"]] = relationship(secondary='patient_appointments', back_populates="appointments") #NEW LINE

patient_appointments = db.Table( #NEW TABLE
    'patient_appointments',
    db.metadata,
    Column('patient_id', Integer, ForeignKey("patients.id"), primary_key=True),
    Column('appointment_id', Integer, ForeignKey("appointments.id"), primary_key=True),
)