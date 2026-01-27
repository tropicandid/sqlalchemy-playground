from models import Patient, Appointment
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
                return make_response(jsonify({"error": "Request body must be JSON"}), 400)

            if missing:
                return jsonify(error="Missing required fields", fields=list(missing)), 400

            new_patient = Patient(
                name=request.json.get("name"),
                birthday=request.json.get("birthday"),
                address=request.json.get("address"),
                phone_number=request.json.get("phone")
            )

            #TODO: verify data types
            try:
                db.session.add(new_patient)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to create patient"), 500
            return jsonify(new_patient.to_dict()), 201


        @app.route(f'/{REST_ROOT}patient/', methods=['GET'])
        def get_patient():
            pass

        @app.route(f'/{REST_ROOT}patient/update/<int:patient_id>', methods=['PUT'])
        def update_patient():
            pass

        @app.route(f'/{REST_ROOT}patient/delete/<int:patient_id>', methods=['DELETE'])
        def delete_patient():
            pass

        @app.route(f'/{REST_ROOT}appointment/add', methods=['POST'])
        def add_appointment():
            data = request.get_json(silent=True)
            missing = REQUIRED_APPOINTMENT_FIELDS - data.keys()

            if data is None:
                return make_response(jsonify({"error": "Request body must be JSON"}), 400)

            if missing:
                return jsonify(error="Missing required fields", fields=list(missing)), 400

            patient = db.session.execute(db.select(Patient).where(Patient.id == request.json.get("patient_id"))).scalar()
            if not patient:
                return jsonify(error="Unable to locate patient by ID", fields=list(missing)), 400

            new_appointment = Appointment(
                type=request.json.get("type"),
                request_origin=request.json.get("request_origin"),
                date=request.json.get("date"),
                status="scheduled",
                patient=[patient]
            )

            # TODO: verify data types
            try:
                db.session.add(new_appointment)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to create patient"), 500
            return jsonify(new_appointment.to_dict()), 201

        @app.route(f'/{REST_ROOT}appointment/', methods=['GET'])
        def get_appointment():
            pass

        @app.route(f'/{REST_ROOT}appointment/update/<int:appointment_id>', methods=['PUT'])
        def update_appointment():
            pass

        @app.route(f'/{REST_ROOT}appointment/delete/<int:appointment_id>', methods=['DELETE'])
        def delete_appointment():
            pass