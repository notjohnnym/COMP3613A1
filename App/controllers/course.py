from App.models import Course
from App.database import db

def create_course(code, title, credits, semester, faculty):
    course = Course(code, title, credits, semester, faculty)
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

