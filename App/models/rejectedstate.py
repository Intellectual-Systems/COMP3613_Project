from App.models.applicationstate import ApplicationState

class RejectedState(ApplicationState):

    def __init__(self, description=None):
        super().__init__('Rejected', description)

    def shortlist(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_accept(self, application):
        raise Exception("Applicant has already been rejected for this position.")
    
    def employer_reject(self, application):
        raise Exception("Applicant has already been rejected for this position.")