from App.database import db

class Course(db.Model):
    code = db.Column(db.Integer, primary_key = True)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'))
    ta_id = db.Column(db.Integer, db.ForeignKey('ta.id'))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'))
    title = db.Column(db.String(120), nullable = False)
    credits = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    faculty = db.Column(db.String(120), nullable = False)
    
    def __init__ (self, code, title, credits, semester, faculty):
        self.code = code
        self.title = title
        self.credits = credits
        self.semester = semester
        self.faculty = faculty
    
    def get_json(self):
        return{
            'code': self.code,
            'title': self.title,
            'credits': self.credits,
            'semester': self.semester,
            'faculty': self.faculty
        }

