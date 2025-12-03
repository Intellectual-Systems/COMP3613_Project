from App.models.applicationstate import ApplicationState

class ShortlistedState(ApplicationState):

    def __init__(self, description=None):
        super().__init__('Shortlisted', description)

    def shortlist(self, application):
        raise Exception("Application is already shortlisted for a position.")
    
    def employer_accept(self, application):
        application.state = "Accepted"
    
    def employer_reject(self, application):
        application.state = "Rejected"