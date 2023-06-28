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
            Subject(name="Defense Against the Dark Arts"),
            Subject(name="Herbology"),
            Subject(name="Divination"),
            Subject(name="Care of Magical Creatures"),
            Subject(name="Charms"),
            Subject(name="Ancient Runes"),

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

        print("📚 Seeding class enrollments...")
        subject_enrollments = []
        for subject in subjects:
            student = rc(students)
            subject_enrollments.append(
                SubjectEnrollment(subject=subject, student=student, price = randrange(1996, 2003))
            )
        db.session.add_all(subject_enrollments)
        db.session.commit()

        print("⚡️ Done seeding!")
