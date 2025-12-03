from App.models import db
from App.models.applicationstate import ApplicationState

class RejectedState(ApplicationState):
    __tablename__ = 'rejected_state'
    id = db.Column(db.Integer, db.ForeignKey('application_state.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'rejected_state',
    }

    def __init__(self, description=None):
        super().__init__('Rejected', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_reject(self, application):
        raise Exception("Applicant has already been rejected for this position.")