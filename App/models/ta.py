from .staff import Staff
from App.database import db

class TA(Staff):
    __tablename__ = 'ta'
    
    def __init__ (self, id, firstname, lastname, faculty, department):
        super().__init__(id, firstname, lastname, faculty, department)
        self.staff_type = "ta"

