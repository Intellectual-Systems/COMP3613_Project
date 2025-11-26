from App.database import db
from App.models.student import Student
from App.models.position import Position

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer), db.ForeignKey('student.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, applicant_name, position_id, status):
        self.applicant_name = applicant_name
        self.position_id = position_id
        self.status = status