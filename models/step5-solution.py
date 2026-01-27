from extensions import db
from sqlalchemy import Integer, String, Column, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column

##TODO: Step 5
# 1. Create a method to return records in a dictionary format
class Patient(db.Model):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    birthday: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(500))
    phone_number: Mapped[str] = mapped_column(String(15))
    appointments: Mapped[List["Appointment"]] = relationship(secondary='patient_appointments', back_populates="patient")

    def to_dict(self): #NEW METHOD
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    request_origin: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    patient: Mapped[List["Patient"]] = relationship(secondary='patient_appointments', back_populates="appointments")

    def to_dict(self): #NEW METHOD
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

patient_appointments = db.Table(
    'patient_appointments',
    db.metadata,
    Column('patient_id', Integer, ForeignKey("patients.id"), primary_key=True),
    Column('appointment_id', Integer, ForeignKey("appointments.id"), primary_key=True),
)