from App.database import db
from App.models.position import Position
from App.models.applicationstate import ApplicationState

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    # application_state = db.Column(db.String(50), db.ForeignKey('applicationstate.state'),nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, applicant_name, position_id, status):
        self.applicant_name = applicant_name
        self.position_id = position_id
        self.status = status
        self.application_state = status