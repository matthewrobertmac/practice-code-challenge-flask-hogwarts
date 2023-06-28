import pytest
from app import app
from models import db, Subject, Student, SubjectEnrollment
from faker import Faker


class TestClassEnrollment:
    '''Class VendorSweet in models.py'''

    def test_price_0_or_greater(self):
        '''requires price >= 0.'''

        with app.app_context():

            student = Student(name=Faker().name(), )
            subject = Subject(name=Faker().name())
            db.session.add_all([student, subject])
            db.session.commit()

            subject_enrollment = SubjectEnrollment(
                subject_id=subject.id, student_id=student.id, enrollment_year=2000)
            db.session.add(subject_enrollment)
            db.session.commit()

    def test_price_too_low(self):
        '''requires non negative price .'''

        with app.app_context():

            with pytest.raises(ValueError):
                student = Student(name=Faker().name(), )
                subject = Subject(name=Faker().name())
                db.session.add_all([student, subject])
                db.session.commit()

                subject_enrollment = SubjectEnrollment(
                    subject_id=subject.id, student_id=student.id, enrollment_year=1900)
                db.session.add(subject_enrollment)
                db.session.commit()

    def test_price_none(self):
        '''requires non negative price .'''

        with app.app_context():

            with pytest.raises(ValueError):
                student = Student(name=Faker().name(), )
                subject = Subject(name=Faker().name())
                db.session.add_all([student, subject])
                db.session.commit()

                subject_enrollment = SubjectEnrollment(
                    subject_id=subject.id, student_id=student.id, enrollment_year=1900)
                db.session.add(subject_enrollment)
                db.session.commit()
