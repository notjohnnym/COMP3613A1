from App.database import db

class CourseStaff(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_code = (db.String(20), db.ForeignKey('course.code'))
    staff_id = (db.Integer, db.ForeignKey('staff.id'))

    def __init__ (self, code, id):
        self.course_code = code
        self.staff_id = id

