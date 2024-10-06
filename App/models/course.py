from App.database import db

class Course(db.Model):
    __tablename__ = 'course'

    code = db.Column(db.String(20), primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    credit = db.Column(db.Integer, nullable = False)
    semester = db.Column(db.Integer, nullable = False)
    faculty = db.Column(db.String(120), nullable = False)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable = True)
    ta_id = db.Column(db.Integer, db.ForeignKey('ta.id'), nullable = True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable = True)
    
    def __init__ (self, code, title, credit, semester, faculty):
        self.code = code
        self.title = title
        self.credit = credit
        self.semester = semester
        self.faculty = faculty
        self.lecturer_id = None
        self.ta_id = None
        self.tutor_id = None
    
    def assign_lecturer(self, lecturer):
        self.lecturer_id = lecturer.id
        db.session.commit()
    
    def assign_ta(self, ta):
        self.ta_id = ta.id
        db.session.commit()
    
    def assign_tutor(self, tutor):
        self.tutor_id = tutor.id
        db.session.commit()

    def get_json(self):
        return{
            'code': self.code,
            'title': self.title,
            'credit': self.credit,
            'semester': self.semester,
            'faculty': self.faculty
        }

