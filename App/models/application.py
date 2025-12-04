from App.database import db
from App.models.position import Position
from App.models.applicationstate import ApplicationState

class Application(db.Model):
    _tablename_ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    application_state = db.Column(db.String(50), db.ForeignKey('applicationstate.state'),nullable=False)

    def _init_(self, student_id, position_id, state):
        self.student_id = student_id
        self.position_id = position_id
        self.application_state = state