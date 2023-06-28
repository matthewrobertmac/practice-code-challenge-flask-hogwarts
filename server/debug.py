#!/usr/bin/env python3

from app import app
from models import db, Student, Subject, SubjectEnrollment

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()