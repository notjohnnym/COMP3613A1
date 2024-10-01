from App.database import db

class Staff(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(60), nullable = False)
    lastname = db.Column(db.String(60), nullable = False)
    faculty = db.Column(db.String(120), nullable = False)
    department = db.Column(db.String(120), nullable = False)
    staff_type = db.Column(db.String(20))
    
    def __init__ (self, id, firstname, lastname, faculty, department):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.faculty = faculty
        self.department = department
        self.staff_type = None
    
    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'faculty': self.faculty,
            'department': self.department
        }

