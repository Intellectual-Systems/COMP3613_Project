from App.models import db
from App.models.applicationstate import ApplicationState

class ShortlistedState(ApplicationState):
    __tablename__ = 'shortlisted_state'
    id = db.Column(db.Integer, db.ForeignKey('application_state.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'shortlisted_state',
    }

    def __init__(self, description=None):
        super().__init__('Shortlisted', description)

    def shortlist(self, application):
        raise Exception("Application is already shortlisted for a position.")
    
    def employer_accept(self, application):
        application.state = "Accepted"
    
    def employer_reject(self, application):
        application.state = "Rejected"