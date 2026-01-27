# This file has been equipped with the basic class structure and
# module includes to get you started. As you go through the
# steps, you may need to import additional modules or create new
# class structures. For full reference documentation, return to
# the README.md

from extensions import db
from sqlalchemy import Integer, String, Column, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column

##TODO: Step 1
# 1. Create a model with the tablename 'patients'.
# 2. Include columns for ID<int>, Name<string>, Birthday<string>

##TODO: Step 2
# 1. Modify the 'patients' table by adding a column for Address<string> and a column for Phone Number<string>.
# 2. You will need to perform a migration to complete this step
# 3. View your database after to confirm the changes have been applied as desired.

##TODO: Step 3
# 1. Create a model with the tablename 'appointments'.
# 2. Include columns for ID, type, request_origin, date, and status

##TODO: Step 4
# 1. Create a one to many relationship between the 'patients' and 'appointments' tables.

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

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    request_origin: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    patient: Mapped[List["Patient"]] = relationship(secondary='patient_appointments', back_populates="appointments")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

patient_appointments = db.Table(
    'patient_appointments',
    db.metadata,
    Column('patient_id', Integer, ForeignKey("patients.id"), primary_key=True),
    Column('appointment_id', Integer, ForeignKey("appointments.id"), primary_key=True),
)