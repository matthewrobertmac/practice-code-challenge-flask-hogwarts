from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String)

    # Add relationship

    subject_enrollments = db.relationship('SubjectEnrollment', backref='students', cascade="all, delete-orphan")
    
    # Add serialization
    serialize_only = ('id', 'name', 'age')

    # Add validation
    @validates('age') 
    def validate_age(self, key, age):
        if not (11 <= int(age) <= 18):
            raise ValueError("age must be between 11 and 18")
        else:
            return age

    
    
    def __repr__(self):
        return f'<Student {self.id}>'

class Subject(db.Model, SerializerMixin):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    # Add relationship
    subject_enrollments = db.relationship('SubjectEnrollment', backref='subjects', cascade="all, delete-orphan")

    # Add serialization
    serialize_only = ('id', 'title') 
    
    def __repr__(self):
        return f'<Subject {self.id}>'

class SubjectEnrollment(db.Model, SerializerMixin):
    __tablename__ = 'subject_enrollments'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_year = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id')) 

    # Add relationships
    #students = db.relationship('Student', 'subject_enrollment')
    #subjects = db.relationship('Subject', 'subject_enrollment')
    
    # Add serialization
    serialize_only = ('id', 'enrollment_year', 'student_id', 'subject_id') 
    
    # Add validation
    @validates('enrollment_year')
    def validate_enrollment_year(self, key, enrollment_year):
        if not enrollment_year < 2023:
            raise ValueError("enrollment must be before 2023")
        else:
            return enrollment_year
    
    def __repr__(self):
        return f'<SubjectEnrollment {self.id}>'


