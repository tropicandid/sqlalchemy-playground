from models import Patient, Appointment
from flask import request, jsonify, make_response
from sqlalchemy import select

## TODO: Step 1. Add record to tables
# 1. Create rest endpoint that adds a patient record
# 2. Create rest endpoint that adds an appointment record

REST_ROOT = '/sqlalchpg/v1/'
REQUIRED_PATIENT_FIELDS = {"name", "birthday", "address", "phone"}
REQUIRED_APPOINTMENT_FIELDS = {"type", "request_origin", "date", "patient_id"}

class RestRoutes:
    def __init__(self, app, db):

        @app.route('/')
        def get_home():
            return "SQL Alchemy Playground"

        @app.route(f'/{REST_ROOT}patient/add', methods=['POST'])
        def add_patient():
            data = request.get_json(silent=True)
            missing = REQUIRED_PATIENT_FIELDS - data.keys()

            if data is None:
                return make_response(jsonify({"Error": "Request body must be JSON"}), 400)

            if missing:
                return jsonify(error="Missing required fields", fields=list(missing)), 400

            new_patient = Patient(
                name=request.json.get("name"),
                birthday=request.json.get("birthday"),
                address=request.json.get("address"),
                phone_number=request.json.get("phone")
            )

            try:
                db.session.add(new_patient)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to create patient"), 500
            return jsonify(
                {"status": "Success", 'message': "Patient created successfully", "data": new_patient.to_dict()}), 201

        @app.route(f'/{REST_ROOT}appointment/add', methods=['POST'])
        def add_appointment():
            data = request.get_json(silent=True)
            missing = REQUIRED_APPOINTMENT_FIELDS - data.keys()

            if data is None:
                return make_response(jsonify({"Error": "Request body must be JSON"}), 400)

            if missing:
                return jsonify(error="Missing required fields", fields=list(missing)), 400

            patient = db.session.execute(
                db.select(Patient).where(Patient.id == request.json.get("patient_id"))).scalar()
            if not patient:
                return jsonify(error="Unable to locate patient by ID", fields=list(missing)), 400

            new_appointment = Appointment(
                type=request.json.get("type"),
                request_origin=request.json.get("request_origin"),
                date=request.json.get("date"),
                status="scheduled",
                patient=[patient]
            )

            try:
                db.session.add(new_appointment)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to create patient"), 500
            return jsonify({"status": "success", 'message': "Patient created successfully",
                            "data": new_appointment.to_dict()}), 201