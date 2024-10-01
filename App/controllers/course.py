from App.models import Course
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

