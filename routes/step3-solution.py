from models import Patient, Appointment
from flask import request, jsonify, make_response
from sqlalchemy import select

## TODO: Step 3. Update a record / Delete a record
# 1. Create rest endpoint that can update patient data
# 2. Create rest endpoint that can delete a patient record
# 3. Create rest endpoint that can update patient appointment data
# 4. Create rest endpoint that can delete an appointment record

REST_ROOT = '/sqlalchpg/v1/'
REQUIRED_PATIENT_FIELDS = {"name", "birthday", "address", "phone"}
REQUIRED_APPOINTMENT_FIELDS = {"type", "request_origin", "date", "patient_id"}

class RestRoutes:
    def __init__(self, app, db):

        @app.route('/')
        def get_home():
            return "SQL Alchemy Playground"

        @app.route(f'/{REST_ROOT}patient/update/<int:patient_id>', methods=['PUT'])
        def update_patient(patient_id):
            data = request.json
            patient = db.session.scalars(select(Patient).filter_by(id=patient_id)).first()

            if not patient:
                return make_response(jsonify({"Error": "Requested patient ID not found"}), 400)

            for key, value in data.items():
                if hasattr(patient, key):
                    setattr(patient, key, value)
            try:
                db.session.add(patient)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to update patient"), 500

            return jsonify(
                {"status": "Success", "message": "Patient updated successfully.", "data": patient.to_dict()}), 201

        @app.route(f'/{REST_ROOT}patient/delete/<int:patient_id>', methods=['DELETE'])
        def delete_patient(patient_id):
            patient = db.session.scalars(select(Patient).filter_by(id=patient_id)).first()

            if not patient:
                return make_response(jsonify({"Error": "Requested patient ID not found"}), 400)

            try:
                db.session.delete(patient)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to delete patient"), 500

            return jsonify({"status": "success", 'message': "Patient deleted successfully"}), 201

        @app.route(f'/{REST_ROOT}appointment/update/<int:appointment_id>', methods=['PUT'])
        def update_appointment(appointment_id):
            data = request.json
            appointment = db.session.scalars(select(Appointment).filter_by(id=appointment_id)).first()

            if not appointment:
                return make_response(jsonify({"Error": "Requested appointment ID not found"}), 400)

            for key, value in data.items():
                if hasattr(appointment, key):
                    setattr(appointment, key, value)
            try:
                db.session.add(appointment)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to update appointment"), 500

            return jsonify({"status": "success", "message": "Appointment updated successfully.",
                            "data": appointment.to_dict()}), 201

        @app.route(f'/{REST_ROOT}appointment/delete/<int:appointment_id>', methods=['DELETE'])
        def delete_appointment(appointment_id):
            appointment = db.session.scalars(select(Appointment).filter_by(id=appointment_id)).first()

            if not appointment:
                return make_response(jsonify({"Error": "Requested appointment ID not found"}), 400)

            try:
                db.session.delete(appointment)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(error="Failed to delete appointment"), 500

            return jsonify({"status": "success", 'message': "Appointment deleted successfully"}), 201