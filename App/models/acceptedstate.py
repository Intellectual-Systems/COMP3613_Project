from App.models import db
from App.models.applicationstate import ApplicationState

class AcceptedState(ApplicationState):

    def __init__(self, description=None):
        super().__init__('Accepted', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been accepted for a position.")
    
    def employer_reject(self, application):
        raise Exception("Cannot reject an applicant who has already been accepted.")