from models import Patient, Appointment
from flask import request, jsonify, make_response
from sqlalchemy import select

## TODO: Step 2  Retrieve records from table
# 1. Create rest endpoint that can get patient record by ID
# 2. Create rest endpoint that can get appointment record by ID

REST_ROOT = '/sqlalchpg/v1/'
REQUIRED_PATIENT_FIELDS = {"name", "birthday", "address", "phone"}
REQUIRED_APPOINTMENT_FIELDS = {"type", "request_origin", "date", "patient_id"}

class RestRoutes:
    def __init__(self, app, db):

        @app.route('/')
        def get_home():
            return "SQL Alchemy Playground"

        @app.route(f'/{REST_ROOT}patient/<int:patient_id>', methods=['GET'])
        def get_patient(patient_id):
            try:
                patient = db.session.scalars(select(Patient).filter_by(id=patient_id)).first()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to retrieve patient"), 500

            if not patient:
                return make_response(jsonify({"Error": "Requested patient ID not found"}), 400)

            return jsonify({'status': "success", "data": patient.to_dict()}), 201

        @app.route(f'/{REST_ROOT}appointment/<int:appointment_id>', methods=['GET'])
        def get_appointment(appointment_id):
            try:
                appointment = db.session.scalars(select(Appointment).filter_by(id=appointment_id)).first()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to retrieve patient"), 500

            if not appointment:
                return make_response(jsonify({"Error": "Requested patient ID not found"}), 400)

            return jsonify({"status": "success", "data": appointment.to_dict()}), 201