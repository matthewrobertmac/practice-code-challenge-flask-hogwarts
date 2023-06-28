#!/usr/bin/env python3
from models import db, Student, Subject, SubjectEnrollment
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Students(Resource):
    def get(self):
        students = Student.query.all()
        response_body = []
        for student in students:
            response_body.append(student.to_dict())
        return make_response(jsonify(response_body), 200)

api.add_resource(Students, '/students')

class StudentById(Resource):
    def get(self, id):
        student = Student.query.filter_by(id=id).first()
        if not student:
            response_body = {'error': 'Student not found'}
            status = 404
        else:
            response_body = student.to_dict()
            status = 200
        return make_response(response_body, status)

api.add_resource(StudentById, '/students/<int:id>')

class Subjects(Resource):
    def get(self):
        subjects = Subject.query.all()
        response_body = []
        for subject in subjects:
            response_body.append(subject.to_dict())
        return make_response(jsonify(response_body), 200)

api.add_resource(Subjects, '/subjects')

class SubjectById(Resource):
    def get(self, id):
        subject = Subject.query.filter_by(id=id).first()
        if not subject:
            response_body = {'error': 'Subject not found'}
            status = 404
        else:
            response_body = subject.to_dict()
            status = 200
        return make_response(response_body, status)

api.add_resource(SubjectById, '/subjects/<int:id>') 


class SubjectEnrollments(Resource):
    def post(self):
        try:
            new_subject_enrollment = SubjectEnrollment(enrollment_year=request.get_json().get('enrollment_year'), student_id = request.get_json().get('student_id'), subject_id=request.get_json().get('subject_id')) 
            db.session.add(new_subject_enrollment)
            db.session.commit()
            response_body = new_subject_enrollment.to_dict() 
            return make_response(jsonify(response_body), 200)
        except ValueError as error:
            response_body = {'errors': ['validation errors']} 
            return make_response(jsonify(response_body), 422)
        
api.add_resource(SubjectEnrollments, '/subject_enrollments')

class SubjectEnrollmentsById(Resource):
    def delete(self, id):
        subject_enrollment = SubjectEnrollment.query.filter_by(id=id).first() 
        if not subject_enrollment: 
            response_body = {'error': 'Subject Enrollment not found'} 
            return make_response(jsonify(response_body), 404)
        else:
            db.session.delete(subject_enrollment)
            db.session.commit() 
            response_body = {}
            return make_response(jsonify(response_body))

api.add_resource(SubjectEnrollmentsById, '/subject_enrollments/<int:id>')

@app.route('/')
def home():
    return '<h1>🔮 Hogwarts Classes</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
