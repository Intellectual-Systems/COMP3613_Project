from App.database import db
# from App.models.position import Position
from App.models.position import Position
from App.models.applicationstate import ApplicationState, STATE_MAP

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    application_state = db.Column(db.String(50), nullable=False, default='Applied')

    def __init__(self, student_id, position_id):
        self.student_id = student_id
        self.position_id = position_id
        self.application_state = 'Applied'
    
    def __repr__(self):
        return f"Application[id= {self.id}, student_id= {self.student_id}, position_id= {self.position_id}, application_state= {self.application_state}]"
    
    def get_state(self):
        state_class = STATE_MAP.get(self.application_state)
        if state_class:
            return state_class()
        else:
            raise Exception(f"Unknown application state: {self.application_state}")
    
    def set_state(self, new_state):
        if new_state in STATE_MAP:
            self.application_state = new_state
        else:
            raise Exception(f"Invalid state transition to: {new_state}")
    
    def shortlist(self):
        self.get_state().shortlist(self)
    
    def employer_accept(self):
        self.get_state().employer_accept(self)
    
    def employer_reject(self):
        self.get_state().employer_reject(self)
        
    def get_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'position_id': self.position_id,
            'application_state': self.application_state
        }
