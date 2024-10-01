from App.models import Staff, Lecturer, TA, Tutor
from App.database import db

def create_lecturer(id, firstname, lastname, faculty, department):
    lecturer = Lecturer(id, firstname, lastname, faculty, department)
    try:
        db.session.add(lecturer)
        db.session.commit()
        return lecturer
    except:
        return None

def create_ta(id, firstname, lastname, faculty, department):
    ta = TA(id, firstname, lastname, faculty, department)
    try:
        db.session.add(ta)
        db.session.commit()
        return ta
    except:
        return None

def create_tutor(id, firstname, lastname, faculty, department):
    tutor = Tutor(id, firstname, lastname, faculty, department)
    try:
        db.session.add(tutor)
        db.session.commit()
        return tutor
    except:
        return None

def get_lecturer(id):
    return Lecturer.query.get(id)

def get_ta(id):
    return TA.query.get(id)

def get_tutor(id):
    return Tutor.query.get(id)

def get_all_lecturers():
    return Lecturer.query.all()

def get_all_tas():
    return TA.query.all()

def get_all_tutors():
    return Tutor.query.all()


