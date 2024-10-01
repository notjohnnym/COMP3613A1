from .staff import Staff
from App.database import db

class Tutor(Staff):
    __tablename__ = 'tutor'
    
    def __init__ (self, id, firstname, lastname, faculty, department):
        super().__init__(id, firstname, lastname, faculty, department)
        self.type = "tutor"

