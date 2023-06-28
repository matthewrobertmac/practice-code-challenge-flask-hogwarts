from random import choice as rc, randrange

from app import app
from models import db, Subject, Student, SubjectEnrollment

if __name__ == '__main__':
    with app.app_context():
        print("🗑 Clearing db...")
        Subject.query.delete()
        Student.query.delete()
        SubjectEnrollment.query.delete()

        print("🔮 Seeding subjects...")
        subjects = [
            Subject(title="Defense Against the Dark Arts"),
            Subject(title="Herbology"),
            Subject(title="Divination"),
            Subject(title="Care of Magical Creatures"),
            Subject(title="Charms"),
            Subject(title="Ancient Runes"),

        ]

        db.session.add_all(subjects)

        print("🤓 Seeding students..")
        students = [
            Student(name="Hermione Granger", age="12"),
            Student(name="Cedric Diggory", age="14"),
            Student(name="Harry Potter", age="12"),
            Student(name="Ginny Weasley", age="11"),
            Student(name="Ron Weasley", age="12"),
            Student(name="Neville Longbottom", age="12"),
        ]

        db.session.add_all(students)

        # print("📚 Seeding subject enrollments...")
        # subject_enrollments = []
        # for subject in subjects:
        #     student = rc(students)
        #     subject_enrollments.append(
        #         SubjectEnrollment(subject=subject, student=student, enrollment_year = randrange(1996, 2003))
        #     )
        # db.session.add_all(subject_enrollments)
        db.session.commit()

        print("⚡️ Done seeding!")
