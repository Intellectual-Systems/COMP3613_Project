from App.database import db
from App.models.user import User
from sqlalchemy import Enum  
import enum  


class Shortlist(db.Model):
    __tablename__ = 'shortlist'
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    positionID = db.Column(db.Integer, db.ForeignKey('position.id'), primary_key=True)
    status = db.Column(db.String(20), nullable=False, default='pending')
    employer_response = db.Column(db.String(20), nullable=True, default=None)

    def __init__(self, studentID, positionID):
        self.studentID = studentID
        self.positionID = positionID
        self.status = 'pending'

    def get_json(self):
        return {
            'studentID': self.studentID,
            'positionID': self.positionID,
            'status': self.status,
            'employer_response': self.employer_response
        }

    def __repr__(self):
        return f"Shortlist[studentID= {self.studentID} -> positionID= {self.positionID}, status= {self.status}, employer_response= {self.employer_response}]"


