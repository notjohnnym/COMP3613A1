from App.models import Course, Lecturer, TA, Tutor
from App.database import db

def create_course(code, title, credit, semester, faculty):
    course = Course(code, title, credit, semester, faculty)
    try:
        db.session.add(course)
        db.session.commit()
        return course
    except:
        return None

def get_course(code):
    return Course.query.get(code)

def get_all_courses():
    return Course.query.all()

def get_all_courses_json():
    courses = Course.query.all()
    if not courses:
        return []
    courses = [course.get_json() for course in courses]
    return courses

def get_staff(code):
    staff = []
    course = get_course(code)
    if course:
        if course.lecturer_id:
            lecturer = Lecturer.query.get(course.lecturer_id)
            staff.append(lecturer.get_json())
        if course.ta_id:
            ta = TA.query.get(course.ta_id)
            staff.append(ta.get_json())
        if course.tutor_id:
            tutor = Tutor.query.get(course.tutor_id)
            staff.append(tutor.get_json())
        return staff
    return None

