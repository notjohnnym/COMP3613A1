from App.database import db

class Course(db.Model):
    __tablename__ = 'course'

    code = db.Column(db.String(20), primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    credit = db.Column(db.Integer, nullable = False)
    semester = db.Column(db.Integer, nullable = False)
    faculty = db.Column(db.String(120), nullable = False)
    
    def __init__ (self, code, title, credit, semester, faculty):
        self.code = code
        self.title = title
        self.credit = credit
        self.semester = semester
        self.faculty = faculty
    
    def get_json(self):
        return{
            'code': self.code,
            'title': self.title,
            'credit': self.credit,
            'semester': self.semester,
            'faculty': self.faculty
        }

