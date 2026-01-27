# from models import Patient, Appointment # Your models may differ. Here is an example
from flask import request, jsonify, make_response
from sqlalchemy import select

## TODO: Step 1. Add record to tables
# 1. Create rest endpoint that adds a patient record
# 2. Create rest endpoint that adds an appointment record

## TODO: Step 2  Retrieve records from table
# 1. Get all patient records
# 2. Get patient record by name or birthday
# 3. Get appointments for given patient

## TODO: Step 3. Update a record / Delete a record
# 1. Change patient appointment date
# 2. Update address or phone number for a patient
# 3. Delete an appointment & relationship record

class RestRoutes:
    def __init__(self, app, db):

        @app.route('/')
        def get_home():
            return "SQL Alchemy Playground"
