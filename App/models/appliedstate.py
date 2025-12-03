from App.models.applicationstate import ApplicationState

class AppliedState(ApplicationState):

    def __init__(self, description=None):
        super().__init__('Applied', description)

    def shortlist(self, application):
        application.state = "Shortlisted"
    
    def employer_accept(self, application):
        raise Exception("Applicant must be shortlisted before acceptance.")
    
    def employer_reject(self, application):
        raise Exception("Applicant must be shortlisted before rejection.")