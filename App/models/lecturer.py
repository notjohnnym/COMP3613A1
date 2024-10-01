from .staff import Staff
from App.database import db

class Lecturer(Staff):
    __tablename__ = 'lecturer'
    
    def __init__ (self, id, firstname, lastname, faculty, department):
        super().__init__(id, firstname, lastname, faculty, department)
        self.type = "lecturer"

