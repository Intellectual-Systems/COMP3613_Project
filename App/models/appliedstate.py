from App.models import db
from App.models.applicationstate import ApplicationState

class AppliedState(ApplicationState):
    __tablename__ = 'applied_state'
    id = db.Column(db.Integer, db.ForeignKey('application_state.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'applied_state',
    }

    def __init__(self, description=None):
        super().__init__('Applied', description)

    def shortlist(self, application):
        application.state = "Shortlisted"
    
    def employer_accept(self, application):
        raise Exception("Applicant must be shortlisted before acceptance.")
    
    def employer_reject(self, application):
        raise Exception("Applicant must be shortlisted before rejection.")