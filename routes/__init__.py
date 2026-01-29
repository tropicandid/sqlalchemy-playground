from models import Patient, Appointment
from flask import request, jsonify, make_response
from sqlalchemy import select

## TODO: Step 1. Add record to tables
# 1. Create rest endpoint that adds a patient record
# 2. Create rest endpoint that adds an appointment record

## TODO: Step 2  Retrieve records from table
# 1. Create rest endpoint that can get patient record by ID
# 2. Create rest endpoint that can get appointment record by ID

## TODO: Step 3. Update a record / Delete a record
# 1. Create rest endpoint that can change patient appointment data
# 2. Create rest endpoint that can update patient data
# 3. Create rest endpoint that can delete an appointment record
# 4. Create rest endpoint that can delete a patient record

class RestRoutes:
    def __init__(self, app, db):

        @app.route('/')
        def get_home():
            return "SQL Alchemy Playground"